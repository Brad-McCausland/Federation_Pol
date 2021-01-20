import sys
import json
import numpy

from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.Qt import QStandardItemModel, QStandardItem

sys.path.append("./Objects/")
from NationModel import NationModel
from PopulationModel import PopulationModel
from PopulationMetrics import *

QtDesignerFile = "FederationUi.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(QtDesignerFile)

def load_nations():
    data = {}
    nation_dict = []
    with open('json/default_nations.json') as file:
        data = json.load(file)
    for nation_data in data["nations"]:
        nation_dict.append(NationModel(nation_data))

    return nation_dict


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        nations = load_nations()

        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setWindowTitle("Federation")
        self.setupUi(self)


        tree_model = QStandardItemModel()
        root_node = tree_model.invisibleRootItem()

        for nation in nations:
            root_node.appendRow(nation)

        self.NationTreeView.setModel(tree_model)

        population = PopulationModel()

        print(population.countForMetrics(POP_METRIC_SPECIES.HUMAN))
        print(population.countForMetrics(POP_METRIC_APPROVAL.APPROVES))
        print(population.countForMetrics(POP_METRIC_NATIONALITY.HUMAN))
        print(population.countForMetrics(POP_METRIC_NATIONALITY.NORRIK))

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
