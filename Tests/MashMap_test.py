import unittest
from enum import Enum
from Objects import MashMap

class ENUM_SPECIES(Enum):
    TALAXIAN = "1"
    BAJORAN = "2"
    KLINGON = "3"
    CARDASSIAN = "4"

class ENUM_FOOD(Enum):
    LEOLA_ROOT = "1"
    HASPERAT = "2"
    GAGH = "3"
    KANAR = "4"

class ENUM_JOB(Enum):
    CHEF = "1"
    VEDEC = "2"
    WARRIOR = "3"
    ADMIN = "4"

class MashMapTests(unittest.TestCase):

    ################### test exceptions ###################

    # Only enums may be used as metrics
    def test_metrics_are_enums_only(self):
        try:
            mashmap = MashMap.MashMap(1, 2)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    # Setting a value in a cell requires a complete list of metrics
    def test_set_cell_value_requires_complete_metric_set(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)

        # Test for false positive
        try:
            mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT, ENUM_JOB.ADMIN)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

        try:
            mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.setValueForMetrics(1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # Modifying a value in a cell requires a complete list of metrics
    def test_modify_cell_value_requires_complete_metric_set(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)

        # Test for false positive
        try:
            mashmap.modifyValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT, ENUM_JOB.ADMIN)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

        try:
            mashmap.modifyValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.modifyValueForMetrics(1, ENUM_SPECIES.CARDASSIAN)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.modifyValueForMetrics(1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
    
    def test_migrate_values_requires_int(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        mashmap.setValueForMetrics(0, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC)

        # Test for false positive
        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(True)
        except TypeError:
            self.assertTrue(False)

        try:
            mashmap.migrateValuesForMetrics("string", [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
    
    def test_migrate_values_cannot_be_negative(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        mashmap.setValueForMetrics(0, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC)

        # Test for false positive
        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(True)
        except TypeError:
            self.assertTrue(False)

        try:
            mashmap.migrateValuesForMetrics(-1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
    
    def test_migrate_values_must_have_correct_number_of_metrics(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        mashmap.setValueForMetrics(0, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC)

        # Test for false positive
        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_JOB.ADMIN, ENUM_JOB.ADMIN, ENUM_FOOD.KANAR], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            mashmap.migrateValuesForMetrics(1, [ENUM_JOB.ADMIN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC, ENUM_FOOD.KANAR])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

################### end test exceptions ###################

################### test exceptions ###################

    # A new mashmap should have no data
    def test_empty_mashmap_empty(self):
        mashmap = MashMap.MashMap()
        self.assertTrue(mashmap.countForMetrics() == 0)

    # A mashmap that has metrics defined but has not had data set should have no data
    def test_new_mashmap_empty(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        self.assertTrue(mashmap.countForMetrics() == 0)

    # Data set for a single cell should be retrievable using the same metrics that defined the cell
    def test_values_retrievable(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.TALAXIAN, ENUM_JOB.CHEF)
        self.assertTrue(mashmap.countForMetrics(ENUM_SPECIES.TALAXIAN, ENUM_JOB.CHEF) == 1)

    # Data should be aggregated into larger numbers when queried using metrics which define a superset
    def test_values_retrievable_across_slices(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.CHEF)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.KLINGON, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.ADMIN)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.KLINGON,  ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.VEDEC)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.KANAR, ENUM_JOB.ADMIN)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.BAJORAN,  ENUM_FOOD.HASPERAT, ENUM_JOB.VEDEC)
        mashmap.setValueForMetrics(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.KANAR, ENUM_JOB.ADMIN)

        self.assertTrue(mashmap.countForMetrics(ENUM_SPECIES.TALAXIAN) == 4)
        self.assertTrue(mashmap.countForMetrics(ENUM_SPECIES.BAJORAN)  == 1)
        self.assertTrue(mashmap.countForMetrics(ENUM_FOOD.LEOLA_ROOT)  == 3)
        self.assertTrue(mashmap.countForMetrics(ENUM_FOOD.KANAR)  == 2)
        self.assertTrue(mashmap.countForMetrics(ENUM_JOB.ADMIN) == 3)
        self.assertTrue(mashmap.countForMetrics(ENUM_JOB.VEDEC) == 2)

        self.assertTrue(mashmap.countForMetrics(ENUM_SPECIES.TALAXIAN, ENUM_FOOD.LEOLA_ROOT) == 2)
        self.assertTrue(mashmap.countForMetrics(ENUM_SPECIES.TALAXIAN, ENUM_JOB.ADMIN) == 2)
        self.assertTrue(mashmap.countForMetrics(ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR) == 2)

if __name__ == '__main__':
    unittest.main()