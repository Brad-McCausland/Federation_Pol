# Multi-dimensional model to represent demographic info

import numpy
import sys
from PyQt5.Qt import QStandardItem
from PopulationEnums import *

class PopulationModel(QStandardItem):
    def __init__(self, popData=dict):
        super().__init__()


        # Basic 2d system
        #                  SPECIES
        #             Human Wutari Mixed
        # Employed      '     '      '
        # Unemployed    '     '      '

        """
        METRICS
        * = maybe
        Species: Species Enum
        Nationality: Nationality Enum
        Employment by sector: Employment enum (agriculture, industry, service, tourism, etc. plus unemployment)
        Poverty rate: % range
        Age: int range
        Political opinions: Range between liberal/conservative. Extremists at either end. Bell curve. Affects elections.
        Govt Approval: % range
        """

        # Smaller, easier to comprehend dataset for testing
        #self.simpleData = [[1 for i in POP_ENUM_SPECIES.__members__] for i in POP_ENUM_NATIONALITY.__members__]
        self.data = numpy.array([[[[[[[1 for i in POP_ENUM_APPROVAL.__members__] for i in POP_ENUM_BELIEFS.__members__] for i in POP_ENUM_AGE.__members__] for i in POP_ENUM_SOCIOECO.__members__] for i in POP_ENUM_EMPLOYMENT.__members__] for i in POP_ENUM_NATIONALITY.__members__] for i in POP_ENUM_SPECIES.__members__])

        print(self.queryData('e'))

    def queryData(self, slices):
        return numpy.sum(self.data[POP_ENUM_SPECIES.HUMAN.value, :, :, :, :, :, POP_ENUM_APPROVAL.DISAPPROVES.value])