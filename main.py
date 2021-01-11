from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import json

sys.path.append("./Objects/")
from Nation import Nation

def create_window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 1920, 1080)
    win.setWindowTitle("Federation")

    win.show()
    sys.exit(app.exec_())

def load_nations():
    data = {}
    nation_list = []
    with open('json/default_nations.json') as file:
        data = json.load(file)
    for nation_data in data["nations"]:
        nation_list.append(Nation(nation_data))

    return nation_list

nations = load_nations()
for nation in nations:
    print(nation.name)
create_window()