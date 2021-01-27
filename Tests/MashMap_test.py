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

    # Only enums may be used as clusters
    def test_clusters_are_enums_only(self):
        try:
            mashmap = MashMap.MashMap(1, 2)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    # Setting a value in a cell requires a complete list of clusters
    def test_set_cell_value_requires_complete_cluster_set(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)

        # Test for false positive
        try:
            mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT, ENUM_JOB.ADMIN)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

        try:
            mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.setValueForClusters(1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # Modifying a value in a cell requires a complete list of clusters
    def test_modify_cell_value_requires_complete_cluster_set(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)

        # Test for false positive
        try:
            mashmap.modifyValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT, ENUM_JOB.ADMIN)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

        try:
            mashmap.modifyValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.HASPERAT)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.modifyValueForClusters(1, ENUM_SPECIES.CARDASSIAN)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
            
        try:
            mashmap.modifyValueForClusters(1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
    
    def test_migrate_values_requires_int(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        mashmap.setValueForClusters(0, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC)

        # Test for false positive
        try:
            mashmap.migrateValuesForClusters(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(True)
        except TypeError:
            self.assertTrue(False)

        try:
            mashmap.migrateValuesForClusters("string", [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
    
    def test_migrate_values_cannot_be_negative(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        mashmap.setValueForClusters(0, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC)

        # Test for false positive
        try:
            mashmap.migrateValuesForClusters(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(True)
        except TypeError:
            self.assertTrue(False)

        try:
            mashmap.migrateValuesForClusters(-1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
    
    def test_migrate_values_must_have_correct_number_of_clusters(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        mashmap.setValueForClusters(0, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC)

        # Test for false positive
        try:
            mashmap.migrateValuesForClusters(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

        try:
            mashmap.migrateValuesForClusters(1, [ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            mashmap.migrateValuesForClusters(1, [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            mashmap.migrateValuesForClusters(1, [ENUM_JOB.ADMIN, ENUM_JOB.ADMIN, ENUM_FOOD.KANAR], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            mashmap.migrateValuesForClusters(1, [ENUM_JOB.ADMIN, ENUM_JOB.ADMIN], [ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC, ENUM_FOOD.KANAR])
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

################### end test exceptions ###################

################### test fault tolerance ###################

    def test_cluster_order_doesnt_matter(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForClusters(1, ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.CARDASSIAN, ENUM_JOB.ADMIN) == 1)
        self.assertTrue(mashmap.countForClusters(ENUM_JOB.ADMIN, ENUM_SPECIES.CARDASSIAN) == 1)

################### end test fault tolerance ###################

################### test operations ###################

    # A new mashmap should have no data
    def test_empty_mashmap_empty(self):
        mashmap = MashMap.MashMap()
        self.assertTrue(mashmap.countForClusters() == 0)

    # A mashmap that has clusters defined but has not had data set should have no data
    def test_new_mashmap_empty(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        self.assertTrue(mashmap.countForClusters() == 0)

    # Data set for a single cell should be retrievable using the same clusters that defined the cell
    def test_values_retrievable(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForClusters(1, ENUM_SPECIES.TALAXIAN, ENUM_JOB.CHEF)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.TALAXIAN, ENUM_JOB.CHEF) == 1)

    # Data should be aggregated into larger numbers when queried using clusters which define a superset
    def test_values_retrievable_across_slices(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)
        mashmap.setValueForClusters(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.CHEF)
        mashmap.setValueForClusters(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR)
        mashmap.setValueForClusters(1, ENUM_SPECIES.KLINGON, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR)
        mashmap.setValueForClusters(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.ADMIN)
        mashmap.setValueForClusters(1, ENUM_SPECIES.KLINGON,  ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.VEDEC)
        mashmap.setValueForClusters(1, ENUM_SPECIES.TALAXIAN, ENUM_FOOD.KANAR, ENUM_JOB.ADMIN)
        mashmap.setValueForClusters(1, ENUM_SPECIES.BAJORAN,  ENUM_FOOD.HASPERAT, ENUM_JOB.VEDEC)
        mashmap.setValueForClusters(2, ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.KANAR, ENUM_JOB.ADMIN)

        # One cluster
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.TALAXIAN) == 4)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN)  == 1)
        self.assertTrue(mashmap.countForClusters(ENUM_FOOD.LEOLA_ROOT)  == 3)
        self.assertTrue(mashmap.countForClusters(ENUM_FOOD.KANAR) == 3)
        self.assertTrue(mashmap.countForClusters(ENUM_JOB.ADMIN) == 4)
        self.assertTrue(mashmap.countForClusters(ENUM_JOB.VEDEC) == 2)

        # Two clusters
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.TALAXIAN, ENUM_FOOD.LEOLA_ROOT) == 2)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.TALAXIAN, ENUM_JOB.ADMIN) == 2)
        self.assertTrue(mashmap.countForClusters(ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR) == 2)

        # Three clusters
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN,  ENUM_FOOD.HASPERAT, ENUM_JOB.VEDEC) == 1)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.KANAR, ENUM_JOB.ADMIN) == 2)
        
        # Verify empty cells
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_FOOD.GAGH) == 0)
        self.assertTrue(mashmap.countForClusters(ENUM_FOOD.GAGH, ENUM_JOB.CHEF) == 0)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.KLINGON, ENUM_JOB.ADMIN) == 0)


    def test_migration_operations(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        mashmap.setValueForClusters(6, ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR)
        mashmap.setValueForClusters(3, ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC)

        mashmap.migrateValuesForClusters(1, [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR], [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 5)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 4)

        mashmap.migrateValuesForClusters(2, [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC], [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 7)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 2)

        # Verify can't reduce count below zero
        mashmap.migrateValuesForClusters(10, [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC], [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 9)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 0)


if __name__ == '__main__':
    unittest.main()