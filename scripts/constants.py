API_KEY = "a77a95770c765160cab9847418d50e77a2f50f0d"

CENSUS_API_URL = "https://api.census.gov/data/2022/acs/acs5"
CENSUS_VARIABLES_URL = "https://api.census.gov/data/2023/acs/acs1/variables.html"

POPULATION_DATA_PATH = "data/population/"
HOUSEHOLD_DATA_PATH = "data/household/"

AGE_GROUP_MAPPING = {
    "adult_list": [
        "20t21", "22t24", "25t29", "30t34", "35t39", "40t44", "45t49", 
        "50t54", "55t59", "60t61", "62t64", "65t66", "67t69", "70t74", 
        "75t79", "80t84", "85plus"
    ],
    "children_list": ["U5", "5t9", "10t14", "15t17", "18t19"]
}

AGE_PATTERNS = [
        (r'Under 5 years', 'U5'),
        (r'5 to 9 years', '5t9'),
        (r'10 to 14 years', '10t14'),
        (r'15 to 17 years', '15t17'),
        (r'18 and 19 years', '18t19'),
        (r'20 years', '20'),
        (r'21 years', '21'),
        (r'22 to 24 years', '22t24'),
        (r'25 to 29 years', '25t29'),
        (r'30 to 34 years', '30t34'),
        (r'35 to 39 years', '35t39'),
        (r'40 to 44 years', '40t44'),
        (r'45 to 49 years', '45t49'),
        (r'50 to 54 years', '50t54'),
        (r'55 to 59 years', '55t59'),
        (r'60 and 61 years', '60t61'),
        (r'62 to 64 years', '62t64'),
        (r'65 and 66 years', '65t66'),
        (r'67 to 69 years', '67t69'),
        (r'70 to 74 years', '70t74'),
        (r'75 to 79 years', '75t79'),
        (r'80 to 84 years', '80t84'),
        (r'85 years and over', '85plus')
    ]

STATE_DICT = {
    "01": ("Alabama", "AL"),
    "02": ("Alaska", "AK"),
    "04": ("Arizona", "AZ"),
    "05": ("Arkansas", "AR"),
    "06": ("California", "CA"),
    "08": ("Colorado", "CO"),
    "09": ("Connecticut", "CT"),
    "10": ("Delaware", "DE"),
    "11": ("District of Columbia", "DC"),
    "12": ("Florida", "FL"),
    "13": ("Georgia", "GA"),
    "15": ("Hawaii", "HI"),
    "16": ("Idaho", "ID"),
    "17": ("Illinois", "IL"),
    "18": ("Indiana", "IN"),
    "19": ("Iowa", "IA"),
    "20": ("Kansas", "KS"),
    "21": ("Kentucky", "KY"),
    "22": ("Louisiana", "LA"),
    "23": ("Maine", "ME"),
    "24": ("Maryland", "MD"),
    "25": ("Massachusetts", "MA"),
    "26": ("Michigan", "MI"),
    "27": ("Minnesota", "MN"),
    "28": ("Mississippi", "MS"),
    "29": ("Missouri", "MO"),
    "30": ("Montana", "MT"),
    "31": ("Nebraska", "NE"),
    "32": ("Nevada", "NV"),
    "33": ("New Hampshire", "NH"),
    "34": ("New Jersey", "NJ"),
    "35": ("New Mexico", "NM"),
    "36": ("New York", "NY"),
    "37": ("North Carolina", "NC"),
    "38": ("North Dakota", "ND"),
    "39": ("Ohio", "OH"),
    "40": ("Oklahoma", "OK"),
    "41": ("Oregon", "OR"),
    "42": ("Pennsylvania", "PA"),
    "44": ("Rhode Island", "RI"),
    "45": ("South Carolina", "SC"),
    "46": ("South Dakota", "SD"),
    "47": ("Tennessee", "TN"),
    "48": ("Texas", "TX"),
    "49": ("Utah", "UT"),
    "50": ("Vermont", "VT"),
    "51": ("Virginia", "VA"),
    "53": ("Washington", "WA"),
    "54": ("West Virginia", "WV"),
    "55": ("Wisconsin", "WI"),
    "56": ("Wyoming", "WY")
}

