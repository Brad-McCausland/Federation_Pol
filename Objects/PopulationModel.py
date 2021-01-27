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

    # Migrate individuals away from the 
    #def biDirectionalRepulsion(self, clusters)

    # Parameters is a tuple. The first element 
    def newRandomMashMap(self, parameters):
        return MashMap(POP_METRIC_SPECIES, POP_METRIC_NATIONALITY, POP_METRIC_EMPLOYMENT, POP_METRIC_SOCIOECO, POP_METRIC_AGE, POP_METRIC_BELIEFS, POP_METRIC_APPROVAL)