import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem

from ShortNameModel import ShortNameModel

# Model object for a single nation. Initialize with a Nation object.

class NationModel(QStandardItem):
    def __init__(self, nation_data=dict):
        super().__init__()
        self.nations = nation_data or []
        self.setEditable(False)
        self.setText(nation_data["name"])
        self.appendRow(ShortNameModel(nation_data["short_name"]))