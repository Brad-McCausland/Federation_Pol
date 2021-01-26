import numpy
import sys
from PyQt5.Qt import QStandardItem
from PopulationMetrics import *
from MashMap import MashMap

# TODO: cache results of frequently-used queries to improve performance?

class PopulationModel(QStandardItem):
    def __init__(self, popData=dict):
        super().__init__()
        self.data = MashMap(POP_METRIC_SPECIES, POP_METRIC_NATIONALITY, POP_METRIC_EMPLOYMENT, POP_METRIC_SOCIOECO, POP_METRIC_AGE, POP_METRIC_BELIEFS, POP_METRIC_APPROVAL)

    def setValueForMetrics(self, value, *metrics):
        self.data.setValueForMetrics(metrics, value)

    def countForMetrics(self, *metrics):
        return self.data.countForMetrics(*metrics)

    # Metrics must be given as lists when defining two slices
    def migrateValuesForMetrics(self, value, fromMetrics, toMetrics):
        self.data.migrateValuesForMetrics(value, fromMetrics, toMetrics)