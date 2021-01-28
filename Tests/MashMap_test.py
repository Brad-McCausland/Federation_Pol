import unittest
from enum import Enum
from Objects import MashMap

# TALAXIAN, BAJORAN, KLINGON, CARDASSIAN | LEOLA_ROOT, HASPERAT, GAGH, KANAR | CHEF, VEDEC, WARRIOR, ADMIN

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

################### test helper methods ###################

    def test_generate_key_from_clusters(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES)
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_SPECIES.CARDASSIAN) == "4")
        
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == "23")
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_JOB.WARRIOR, ENUM_SPECIES.BAJORAN) == "23")
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_SPECIES.BAJORAN) == "2*")
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_JOB.WARRIOR,) == "*3")

        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_SPECIES.BAJORAN, ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.WARRIOR) == "213")
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.WARRIOR) == "*13")
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == "2*3")
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_FOOD.LEOLA_ROOT, ENUM_JOB.WARRIOR) == "*13")
        
        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_JOB.WARRIOR, ENUM_FOOD.LEOLA_ROOT, ENUM_SPECIES.BAJORAN) == "213")

        self.assertTrue(mashmap.generateKeyFromClusters(ENUM_JOB.WARRIOR) == "**3")

    def test_generate_key_set_from_clusters(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES)
        self.assertTrue(mashmap.completeKeySetForClusters(ENUM_SPECIES.CARDASSIAN) == ["4"])
        
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        set1 = mashmap.completeKeySetForClusters(ENUM_SPECIES.BAJORAN)
        self.assertTrue("21" in set1)
        self.assertTrue("22" in set1)
        self.assertTrue("23" in set1)
        self.assertTrue("24" in set1)

        set2 = mashmap.completeKeySetForClusters(ENUM_JOB.VEDEC)
        self.assertTrue(len(set2) == 4)
        self.assertTrue("12" in set2)
        self.assertTrue("22" in set2)
        self.assertTrue("32" in set2)
        self.assertTrue("42" in set2)


        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)
        set3 = mashmap.completeKeySetForClusters(ENUM_FOOD.GAGH)

        self.assertTrue(len(set3) == 16)
        self.assertTrue("131" in set3)
        self.assertTrue("132" in set3)
        self.assertTrue("133" in set3)
        self.assertTrue("134" in set3)

        self.assertTrue("231" in set3)
        self.assertTrue("232" in set3)
        self.assertTrue("233" in set3)
        self.assertTrue("234" in set3)

        self.assertTrue("331" in set3)
        self.assertTrue("332" in set3)
        self.assertTrue("333" in set3)
        self.assertTrue("334" in set3)

        self.assertTrue("431" in set3)
        self.assertTrue("432" in set3)
        self.assertTrue("433" in set3)
        self.assertTrue("434" in set3)

    def test_generate_cluster_sets_from_clusters(self):
        mashmap = MashMap.MashMap(ENUM_SPECIES)
        self.assertTrue(mashmap.completeClusterSetforClusters(ENUM_SPECIES.CARDASSIAN) == [[ENUM_SPECIES.CARDASSIAN]])
        
        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_JOB)
        set1 = mashmap.completeClusterSetforClusters(ENUM_SPECIES.BAJORAN)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_JOB.CHEF] in set1)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC] in set1)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR] in set1)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_JOB.ADMIN] in set1)

        set2 = mashmap.completeClusterSetforClusters(ENUM_JOB.VEDEC)
        self.assertTrue(len(set2) == 4)
        self.assertTrue([ENUM_SPECIES.TALAXIAN, ENUM_JOB.VEDEC] in set2)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC] in set2)
        self.assertTrue([ENUM_SPECIES.KLINGON, ENUM_JOB.VEDEC] in set2)
        self.assertTrue([ENUM_SPECIES.CARDASSIAN, ENUM_JOB.VEDEC] in set2)


        mashmap = MashMap.MashMap(ENUM_SPECIES, ENUM_FOOD, ENUM_JOB)
        set3 = mashmap.completeClusterSetforClusters(ENUM_FOOD.GAGH)

        self.assertTrue(len(set3) == 16)
        self.assertTrue([ENUM_SPECIES.TALAXIAN, ENUM_FOOD.GAGH, ENUM_JOB.CHEF] in set3)
        self.assertTrue([ENUM_SPECIES.TALAXIAN, ENUM_FOOD.GAGH, ENUM_JOB.VEDEC] in set3)
        self.assertTrue([ENUM_SPECIES.TALAXIAN, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR] in set3)
        self.assertTrue([ENUM_SPECIES.TALAXIAN, ENUM_FOOD.GAGH, ENUM_JOB.ADMIN] in set3)

        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_FOOD.GAGH, ENUM_JOB.CHEF] in set3)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_FOOD.GAGH, ENUM_JOB.VEDEC] in set3)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR] in set3)
        self.assertTrue([ENUM_SPECIES.BAJORAN, ENUM_FOOD.GAGH, ENUM_JOB.ADMIN] in set3)

        self.assertTrue([ENUM_SPECIES.KLINGON, ENUM_FOOD.GAGH, ENUM_JOB.CHEF] in set3)
        self.assertTrue([ENUM_SPECIES.KLINGON, ENUM_FOOD.GAGH, ENUM_JOB.VEDEC] in set3)
        self.assertTrue([ENUM_SPECIES.KLINGON, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR] in set3)
        self.assertTrue([ENUM_SPECIES.KLINGON, ENUM_FOOD.GAGH, ENUM_JOB.ADMIN] in set3)

        self.assertTrue([ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.GAGH, ENUM_JOB.CHEF] in set3)
        self.assertTrue([ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.GAGH, ENUM_JOB.VEDEC] in set3)
        self.assertTrue([ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.GAGH, ENUM_JOB.WARRIOR] in set3)
        self.assertTrue([ENUM_SPECIES.CARDASSIAN, ENUM_FOOD.GAGH, ENUM_JOB.ADMIN] in set3)
################### end test helper methods ###################

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
        mashmap.setValueForClusters(10, ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC)

        # verify whole integer operations
        mashmap.migrateValuesForClusters(1, [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR], [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 5)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 11)

        mashmap.migrateValuesForClusters(2, [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC], [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 7)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 9)

        # Verify can't reduce count below zero
        mashmap.migrateValuesForClusters(12, [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC], [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 16)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 0)

        # verify proportional operations
        mashmap.migrateValuesForClusters(0.5, [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR], [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 8)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 8)
        
        mashmap.migrateValuesForClusters(0.75, [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC], [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 14)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 2)
        
        mashmap.migrateValuesForClusters(0.999, [ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR], [ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC])
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.WARRIOR) == 0)
        self.assertTrue(mashmap.countForClusters(ENUM_SPECIES.BAJORAN, ENUM_JOB.VEDEC) == 16)

if __name__ == '__main__':
    unittest.main()