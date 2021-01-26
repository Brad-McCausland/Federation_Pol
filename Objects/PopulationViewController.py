from PyQt5.Qt import QDialog
from PopulationModel import PopulationModel
from PopulationMetrics import *
from PyQt5.QtWidgets import QVBoxLayout
from PopulationPieChart import PopulationPieChart

class PopulationViewController(QDialog):
    def __init__(self, populationModel):
        super().__init__()
        self.populationModel = populationModel
        data = self.generateDataForMetric(POP_METRIC_SPECIES)
        self.populationPieChart = PopulationPieChart("Test", data)

        layout = QVBoxLayout(self)
        layout.addWidget(self.populationPieChart)

    # Metric is one of the 7 metrics used to categorize a population slice
    def generateDataForMetric(self, metric):
        data = []
        for category in metric:
            data.append([category.name, self.populationModel.countForMetrics(category)])

        return data