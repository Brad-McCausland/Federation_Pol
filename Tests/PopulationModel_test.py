import unittest
from enum import Enum
from Objects import PopulationModel, PopulationMetrics, MashMap

class POP_METRIC_SPECIES(Enum):
    HUMAN = "1"
    WUTARI = "2"
    NORRIK = "3"
    ORELLIAN = "4"
    SHOL_KAR = "5"
    LUVERAN = "6"

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

class PopulationModelTests(unittest.TestCase):

    # Only enums may be used as clusters
    def test_bidirectional_repulsion(self):
        mashmap = MashMap.MashMap(POP_METRIC_SPECIES, POP_METRIC_BELIEFS)

        # Init all cells to 24
        for belief in POP_METRIC_BELIEFS:
            mashmap.setValueForClusters(24, POP_METRIC_SPECIES.HUMAN, belief)
            mashmap.setValueForClusters(24, POP_METRIC_SPECIES.WUTARI, belief)

        self.assertTrue(True)