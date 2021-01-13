from PyQt5.Qt import QStandardItem

# Model object for a single nation's short name.

class ShortNameModel(QStandardItem):
    def __init__(self, name=None):
        super().__init__()
        self.setText(name)

class GovernmentTypeModel(QStandardItem):
    def __init__(self, GType=None):
        super().__init__()
        self.setText(GType)

class NationDemonymModel(QStandardItem):
    def __init__(self, demo=None):
        super().__init__()
        self.setText(demo)

class LeaderModel(QStandardItem):
    def __init__(self, leader=None):
        super().__init__()
        self.setText(leader)