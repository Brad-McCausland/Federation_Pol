# File which defines population metric enums and an abstract class which stores metric metadata as static properties.
# A metric is an enum. Each and every individual can be fully described by a combination of the seven metrics.
# A cluster is a specific value for a metric. The approval metric has two clusters. Individuals are defined by their clusters, not metrics
# An individual or group must have one cluster for seven metrics defined. Partial or null values are not allowed.

from enum import Enum

# Abstract class which holds static properties which relate to population metrics
# TODO: Possible to derive these values? Hard coding bad.
class PopulationMetrics():

    # Total number of metrics defined in this file
    TOTAL_METRIC_COUNT = 7

    # Number of different clusters for each metric
    METRIC_CLUSTER_COUNTS = [6, 6, 9, 6, 7, 9, 2]

# TODO: add generic enums to accomodate randomly generated species?
class POP_METRIC_SPECIES(Enum):
    HUMAN = "1"
    WUTARI = "2"
    NORRIK = "3"
    ORELLIAN = "4"
    SHOL_KAR = "5"
    LUVERAN = "6"

class POP_METRIC_NATIONALITY(Enum):
    HUMAN = "1"
    WUTARI = "2"
    NORRIK = "3"
    ORELLIAN = "4"
    SHOL_KAR = "5"
    LUVERAN = "6"

class POP_METRIC_EMPLOYMENT(Enum):
    UNEMPLOYED = "1"
    AGRICULTURE = "2"
    RESOURCE_EXTRACTION = "3"
    INDUSTRIAL = "4"
    TOURISM = "5"
    FINANCE = "6"
    ACADEMIC = "7"
    ENTERTAINMENT = "8"
    GOVERNMENT_MILITARY = "9"

class POP_METRIC_SOCIOECO(Enum):
    POVERTY = "1"
    LOWER = "2"
    LOWER_MIDDLE = "3"
    MIDDLE = "4"
    UPPER_MIDDLE = "5"
    UPPER = "6"

class POP_METRIC_AGE(Enum):
    POP_20_UNDER = "1"
    POP_21_30 = "2"
    POP_31_40 = "3"
    POP_41_50 = "4"
    POP_51_60 = "5"
    POP_61_70 = "6"
    POP_71_OVER = "7"

class POP_METRIC_BELIEFS(Enum):
    RADICAL_LEFT = "1"
    FAR_LEFT = "2"
    LEFT = "3"
    CENTER_LEFT = "4"
    CENTER = "5"
    CENTER_RIGHT = "6"
    RIGHT = "7"
    FAR_RIGHT = "8"
    RADICAL_RIGHT = "9"

class POP_METRIC_APPROVAL(Enum):
    APPROVES = "1"
    DISAPPROVES = "2"