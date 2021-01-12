from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem

# Model object for a single nation's short name.

class ShortNameModel(QStandardItem):
    def __init__(self, name=None):
        super().__init__()
        self.setEditable(True)
        self.setText(name)