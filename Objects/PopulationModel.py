import numpy
import sys
from PyQt5.Qt import QStandardItem
from PopulationMetrics import *

# TODO: cache frequently-used results to improve performance?
# self.data is dict.
# Key: A string of seven numbers "#######" representing a combination of the seven demographic metrics. The numbers come from their specific metric's enum value.
# Value: The numbers of beings in the population who conform to the combination of metrics defined by the key.

class PopulationModel(QStandardItem):
    def __init__(self, popData=dict):
        super().__init__()
        self.data = {} #TODO: Accept popData if not null

    # Return total count for all kays that comply with given metrics
    def countForMetrics(self, *metrics):
        allMetrics = self.completeKeySetForMetrics(*metrics)
        total = 0
        for metric in allMetrics:
            try:
                total += self.data["".join(metric)]
            except KeyError:
                continue

        return total

    # Enumerate and return list of all possible keys that conform to the given metrics: "111111*" -> ["1111111", "1111112"]
    def completeKeySetForMetrics(self, *metrics):

        baseKey = self.generateBaseKeyFromMetrics(*metrics)
        allKeys = [baseKey]

        # For each index in a key
        for i in range(0, PopulationMetrics.TOTAL_METRIC_COUNT):

            # If index is not specified by a metric in arguments...
            if (baseKey[i] == "*"):
                newKeys = []

                # Combine all current possible keys with all possible values of current index to generate new list of possible keys
                for key in allKeys:
                    for j in range(1, PopulationMetrics.MEMBER_METRIC_COUNTS[i] + 1):
                        newKey = key.copy()
                        newKey[i] = str(j)
                        newKeys.append(newKey)

                    # Replace previous iteration of keys. No keys in output should have '*'
                    allKeys = newKeys

        return allKeys
            
    # Generate a unique, ordered key for an arbitrary list of population enums. Unspecified metrics are left as wildcards.
    def generateBaseKeyFromMetrics(self, *metrics):
        key = ["*","*","*","*","*","*","*"]

        for metric in metrics:
            index = self.indexOfMetric(metric)
            key[index] = metric.value
        
        return key
    
    # Return index in key for metric of given type. Strict ordering is important to prevent collisions/duplications.
    def indexOfMetric(self, metric):
        if isinstance(metric, POP_METRIC_SPECIES):
            return 0
        elif isinstance(metric, POP_METRIC_NATIONALITY):
            return 1
        elif isinstance(metric, POP_METRIC_EMPLOYMENT):
            return 2
        elif isinstance(metric, POP_METRIC_SOCIOECO):
            return 3
        elif isinstance(metric, POP_METRIC_AGE):
            return 4
        elif isinstance(metric, POP_METRIC_BELIEFS):
            return 5
        elif isinstance(metric, POP_METRIC_APPROVAL):
            return 6