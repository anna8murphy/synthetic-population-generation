import vaex
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import math
import time

def load_parquet_agents(file_path, columns=None):
    """
    Generic data loader for agent parquet files.
    
    Parameters:
    file_path (str): Path to the parquet file
    columns (list, optional): List of column names to load. If None, loads all columns.
    
    Returns:
    vaex.DataFrame: DataFrame containing the agent data
    """
    try:
        df = vaex.open(file_path)
        
        # If specific columns are requested, select only those
        if columns is not None:
            available_cols = set(df.column_names)
            valid_cols = [col for col in columns if col in available_cols]
            if not valid_cols:
                raise ValueError(f"None of the requested columns {columns} found in the file")
            df = df[valid_cols]
        
        return df
    
    except Exception as e:
        print(f"Error loading parquet file {file_path}: {e}")
        return None

def process_file_batch(file_paths, columns=None):
    """Helper function to process a batch of files"""
    dfs = []
    for file_path in file_paths:
        try:
            df = load_parquet_agents(str(file_path), columns)
            if df is not None:
                dfs.append(df)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    return dfs

def load_agent_files(base_dir, num_workers=8, batch_size=1000, columns=None):
    """
    Load and process multiple agent parquet files in parallel.
    
    Parameters:
    base_dir (str): Base directory containing agent parquet files
    num_workers (int): Number of parallel workers for loading
    batch_size (int): Number of files to process in each batch
    columns (list, optional): List of column names to load
    
    Returns:
    vaex.DataFrame: Concatenated DataFrame containing all agent data
    """

    # Get all parquet files recursively
    all_files = list(Path(base_dir).rglob("*.parquet"))
    total_files = len(all_files)
    print(f"Found {total_files} parquet files")
    
    # Process files in batches to manage memory
    num_batches = math.ceil(total_files / batch_size)
    all_dfs = []
    
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for batch_idx in range(num_batches):
            
            start_idx = batch_idx * batch_size
            end_idx = min((batch_idx + 1) * batch_size, total_files)
            batch_files = all_files[start_idx:end_idx]
            
            print(f"Processing batch {batch_idx + 1}/{num_batches} ({start_idx} to {end_idx})")
            
            # Split batch into chunks for parallel processing
            chunk_size = math.ceil(len(batch_files) / num_workers)
            chunks = [batch_files[i:i + chunk_size] for i in range(0, len(batch_files), chunk_size)]
            
            # Process chunks in parallel
            futures = [executor.submit(process_file_batch, chunk, columns) for chunk in chunks]
            
            # Collect results
            for future in futures:
                batch_dfs = future.result()
                all_dfs.extend(batch_dfs)
            
            # Periodically concatenate to free memory
            if len(all_dfs) > num_workers * 2:
                print("Concatenating intermediate results...")
                all_dfs = [vaex.concat(all_dfs)]

    print("Concatenating final results...")
    final_df = vaex.concat(all_dfs)
    
    print(f"Loaded {len(final_df)} total agents")
    return final_df

def analyze_agents(df):
    """
    Perform basic analysis on the loaded agent data.
    
    Parameters:
    df (vaex.DataFrame): DataFrame containing agent data
    """
    # Get basic statistics
    total_agents = len(df)
    
    print("\nAgent Analysis:")
    print(f"Total agents: {total_agents:,}")
    
    # Column statistics
    print("\nColumn statistics:")
    for column in df.column_names:
        try:
            if df[column].dtype in ['float64', 'int64']:
                stats = {
                    'mean': df[column].mean(),
                    'min': df[column].min(),
                    'max': df[column].max()
                }
                print(f"{column}: {stats}")
        except Exception as e:
            print(f"Could not compute statistics for {column}: {e}")

def export_to_hdf5(df, output_path, chunk_size=1000000):
    """
    Export a Vaex DataFrame to HDF5 format.
    
    Parameters:
    df (vaex.DataFrame): DataFrame to export
    output_path (str): Path where the HDF5 file will be saved
    chunk_size (int): Number of rows to process at once to manage memory
    
    Returns:
    bool: True if export was successful, False otherwise
    """
    try:
        print(f"Exporting DataFrame to {output_path}")
        df.export_hdf5(output_path, progress=True)
        print(f"Successfully exported to {output_path}")
        return True
    except Exception as e:
        print(f"Error exporting to HDF5: {e}")
        return False

# start_time = time.time()
# df = load_agent_files("output_v2/population")
# total_time = time.time() - start_time
# print(f"Total processing time: {total_time:.2f} seconds ({total_time/60:.2f} minutes)")

# analyze_agents(df)