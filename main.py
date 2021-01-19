import sys
import json
import numpy

from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.Qt import QStandardItemModel, QStandardItem

sys.path.append("./Objects/")
from NationModel import NationModel
from PopulationModel import PopulationModel
from PopulationEnums import *

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

        print(len(population.keySetForTags()))
        """
        totalEmployed = sum(population.data[0])
        totalUnemployed = sum(population.data[1])
        totalHumans = sum(population.data[0:len(population.data), 0])
        totalWutari = sum(population.data[0:len(population.data), 1])
        totalMixed = sum(population.data[0:len(population.data), 2])

        self.NewsFeed.append("Total Humans: " + str(totalHumans))
        self.NewsFeed.append("Total Wutari: " + str(totalWutari))
        self.NewsFeed.append("Total Mixed: " + str(totalMixed))
        self.NewsFeed.append("Total Employed: " + str(totalEmployed))
        self.NewsFeed.append("Total Unemployed: " + str(totalUnemployed))
        """

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
