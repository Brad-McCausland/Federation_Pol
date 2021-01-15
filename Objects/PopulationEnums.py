from enum import Enum

"""
        METRICS
        * = maybe
        Species: Species Enum
        Nationality: Nationality Enum
        Employment by sector: Employment enum (agriculture, industry, service, tourism, etc. plus unemployment)
        Poverty rate: % range
        Age: int range
        Political opinions: Range between liberal/conservative. Extremists at either end. Bell curve. Affects elections.
        Govt Approval: % range
"""

# todo: add generic enums to accomodate randomly generated species?
class POP_ENUM_SPECIES(Enum):
    HUMAN = 1
    WUTARI = 2
    NORRIK = 3
    ORELLIAN = 4
    SHOL_KAR = 5
    LUVERAN = 6

class POP_ENUM_NATIONALITY(Enum):
    HUMAN = 1
    WUTARI = 2
    NORRIK = 3
    ORELLIAN = 4
    SHOL_KAR = 5
    LUVERAN = 6

class POP_ENUM_EMPLOYMENT(Enum):
    UNEMPLOYED = 1
    AGRICULTURE = 2
    RESOURCE_EXTRACTION = 3
    INDUSTRIAL = 4
    TOURISM = 5
    FINANCE = 6
    ACADEMIC = 7
    ENTERTAINMENT = 8
    GOVERNMENT_MILITARY = 9

class POP_ENUM_SOCIOECO(Enum):
    POVERTY = 1
    LOWER = 2
    LOWER_MIDDLE = 3
    MIDDLE = 4
    UPPER_MIDDLE = 5
    UPPER = 6

class POP_ENUM_AGE(Enum):
    POP_20_UNDER = 1
    POP_21_30 = 2
    POP_31_40 = 3
    POP_41_50 = 4
    POP_51_60 = 5
    POP_61_70 = 6
    POP_71_OVER = 7

class POP_ENUM_BELIEFS(Enum):
    RADICAL_LEFT = 1
    FAR_LEFT = 2
    LEFT = 3
    CENTER_LEFT = 4
    CENTER = 5
    CENTER_RIGHT = 6
    RIGHT = 7
    FAR_RIGHT = 8
    RADICAL_RIGHT = 9

class POP_ENUM_APPROVAL(Enum):
    APPROVES = 0
    DISAPPROVES = 1

# 6 * 6 * 9 * 6 * 7 * 9 * 2 = 244,944 ints or 0.98 mb