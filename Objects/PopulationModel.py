from PyQt5.Qt import QStandardItemModel
from PopulationMetrics import *
from MashMap import MashMap

# TODO: cache results of frequently-used queries to improve performance?

# Size is an integer that represents the approximate size 
class PopulationModel(QStandardItemModel):
    def __init__(self, size=0, popData=None):
        super().__init__()

        # If no input, create a new blank population
        if popData is None:
            self.data = MashMap(POP_METRIC_SPECIES, POP_METRIC_NATIONALITY, POP_METRIC_EMPLOYMENT, POP_METRIC_SOCIOECO, POP_METRIC_AGE, POP_METRIC_BELIEFS, POP_METRIC_APPROVAL)
        # Create population with pre-made mashmap
        elif isinstance(popData, MashMap):
            self.data = popData
        # Create a new full-random population
        elif popData == 'r':
            fullRandomParameters = [1, [1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                       [1, 1]
                                    ]
            self.data = self.newRandomMashMap(fullRandomParameters)
        # Generate new population mashmap using given parameters
        elif isinstance(popData[0], list):
            self.data = self.newRandomMashMap(popData)

    def setValueForClusters(self, value, *clusters):
        self.data.setValueForClusters(value, *clusters)

    def countForClusters(self, *clusters):
        return self.data.countForClusters(*clusters)

    # Clusters must be given as lists when defining two slices
    def migrateValuesForClusters(self, value, fromClusters, toClusters):
        self.data.migrateValuesForClusters(value, fromClusters, toClusters)

    """
    # Migrate individuals away from the specified cluster in both directions. Should only be used on metrics that represent a gradient where adjacent clusters are related.
    # Strength is a number between 0 and 1. Strength 0 has no effect. Strength 1 completely empties the target cluster.
    def biDirectionalRepulsion(self, cluster, strength, wrapping=False, restrictedClusters=[]):
        if not (strength >= 0 and strength <= 1):
            raise ValueError("Strength must be between or equal to 0 or 1")

        clusterSets = self.completeClusterSetForClusters(cluster, *restrictedClusters)
        targetIndex = self.indexOfCluster(cluster)

        # Reduce value for each cell specified in input
        for clusterSet in clusterSets:
            # And redistribute among adjacent cells
            for i in range(len(self.metrics[targetIndex])):
                migrateAmount = strength / abs(targetIndex - i)
                migrateTargetKey = key
                migrateTargetKey[targetIndex] = i
                self.migrateValuesForClusters(migrateAmount)
    """
        

    # Parameters is a tuple. The first element 
    def newRandomMashMap(self, parameters):
        return MashMap(POP_METRIC_SPECIES, POP_METRIC_NATIONALITY, POP_METRIC_EMPLOYMENT, POP_METRIC_SOCIOECO, POP_METRIC_AGE, POP_METRIC_BELIEFS, POP_METRIC_APPROVAL)