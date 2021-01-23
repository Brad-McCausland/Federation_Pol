import numpy
import sys
from PyQt5.Qt import QStandardItem
from PopulationMetrics import *
from MashMap import MashMap

# TODO: cache frequently-used results to improve performance?
# self.data is dict.
# Key: A string of seven numbers "#######" representing a combination of the seven demographic metrics. The numbers come from their specific metric's enum value.
# Value: The numbers of beings in the population who conform to the combination of metrics defined by the key.

class PopulationModel(QStandardItem):
    def __init__(self, popData=dict):
        super().__init__()
        self.data = MashMap(POP_METRIC_SPECIES, POP_METRIC_NATIONALITY, POP_METRIC_EMPLOYMENT, POP_METRIC_SOCIOECO, POP_METRIC_AGE, POP_METRIC_BELIEFS, POP_METRIC_APPROVAL)

    def setValueForMetrics(self, value, *metrics):
        self.data.setValueForMetrics(metrics, value)

    def countForMetrics(self, *metrics):
        return self.data.countForMetrics(*metrics)

    # Function for moving population from one slice, defined in fromMetrics, to another, defined by toMetrics.
    # 'amount' can be defined as a whole number to move an absolute 
    #def shiftSliceCounts(self, *fromMetrics, *toMetrics, amount)