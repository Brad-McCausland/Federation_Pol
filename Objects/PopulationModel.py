# Multi-dimensional model to represent demographic info

import numpy
import sys
from PyQt5.Qt import QStandardItem
from PopulationEnums import *
        
"""
METRICS
Species: Species Enum
Nationality: Nationality Enum
Employment by sector: Employment enum (agriculture, industry, service, tourism, etc. plus unemployment)
Poverty rate: % range
Age: int range
Political opinions: Range between liberal/conservative. Extremists at either end. Bell curve. Affects elections.
Govt Approval: % range
"""

class PopulationModel(QStandardItem):
    def __init__(self, popData=dict):
        super().__init__()
        self.data = {}

    # Return list of all possible keys that conform to the given tags
    def keySetForTags(self, *tags):

        # Generate a base key using all requested tags
        baseKey = self.generateKeyFromTags(*tags)
        allKeys = [baseKey] #keys with placeholder zeros still inside

        # For each index (out of 7) in a possible key
        for i in range(0, PopulationEnums.TOTAL_TAG_COUNT):

            # If index is not specified in input...
            if (baseKey[i] == '0'):
                newKeys = []

                # Combine all current possible keys with all possible values of current index to generate new list of possible keys
                for key in allKeys:
                    for j in range(1, PopulationEnums.MEMBER_ENUM_COUNTS[i] + 1):
                        newKey = key.copy()
                        newKey[i] = str(j)
                        newKeys.append(newKey)

                    # Replace previous iteration of keys. No keys in output shou,d have '0'
                    allKeys = newKeys

        return allKeys
            



    # Generate a unique, ordered key for an arbitrary list of population enums
    def generateKeyFromTags(self, *tags):
        key = ["0","0","0","0","0","0","0"]

        for tag in tags:
            index = self.indexOfType(tag)
            key[index] = tag.value
        
        return key
    
    # return appropriate index for tag of type. Strict ordering is important to prevent collisions/duplications.
    def indexOfType(self, tag):
        if isinstance(tag, POP_ENUM_SPECIES):
            return 0
        elif isinstance(tag, POP_ENUM_NATIONALITY):
            return 1
        elif isinstance(tag, POP_ENUM_EMPLOYMENT):
            return 2
        elif isinstance(tag, POP_ENUM_SOCIOECO):
            return 3
        elif isinstance(tag, POP_ENUM_AGE):
            return 4
        elif isinstance(tag, POP_ENUM_BELIEFS):
            return 5
        elif isinstance(tag, POP_ENUM_APPROVAL):
            return 6