from PyQt5.QtChart import QChartView, QChart, QPieSeries
from PyQt5.QtGui import QPainter, QColor


class PopulationPieChart(QChartView):

    # Data is a list of tuples. First element in a tuple is a data point's name. The second is the value.
    def __init__(self, title, data):
        #self.setRenderHint(QPainter.Antialiasing)
        super().__init__()
        chart = QChart()
        self.setChart(chart)
        chart.setTitle(title or "")
        chart.addSeries(self.getSeries(data))

    def getSeries(self, data):
        series = QPieSeries()
        for item in data:
            series.append(item[0], item[1])
        return series