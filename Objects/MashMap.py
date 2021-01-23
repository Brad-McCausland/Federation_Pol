from enum import Enum

# TODO: cache frequent queries to improve performance?
# self.data is dict.
# Key: A string of seven numbers "#######" representing a combination of the seven demographic metrics. The numbers come from their specific metric's enum value.
# Value: The numbers of beings in the population who conform to the combination of metrics defined by the key.
# Cell: a single key/value pair.
# Slice: an area of cells defined by set of metrics. A slice defined by a complete set of metrics will be one cell large. A slice defined by the empty set will contains all cells in the mashmap.

# The Mashmap is more efficient than a database or list of individuals with tags when the number of individuals is large and the number of categories is small.
# Categories is a list of enums that are used to define the scope of the mashmap.
class MashMap():

    # Mashmap is initialized with a list of enums; the metrics the mashmap will track. 
    def __init__(self, *metrics):
        super().__init__()
        self.metrics = metrics
        for metric in metrics:
            if not issubclass(metric, Enum):
                raise TypeError("Only enums may be used as mashmap metrics")
                # Accept ints as metrics? Objects?

        self.data = {} #TODO: Accept popData if not null

    # Return total count for all keys that comply with given metrics. Incomplete list of metrics is acceptable.
    def countForMetrics(self, *metrics):
        allMetrics = self.completeKeySetForMetrics(*metrics)
        total = 0
        for metric in allMetrics:
            try:
                total += self.data["".join(metric)]
            except KeyError:
                continue

        return total

    # Define the value for a slice. Requires a complete list of metrics
    def setValueForMetrics(self, value, *metrics):
        if len(metrics) != len(self.metrics):
            raise ValueError("To set values, a complete list of metrics must be specified")

        key = self.generateBaseKeyFromMetrics(*metrics)
        key = "".join(key)
        self.data[key] = value

    # Modify the value of a slice by addition. Value can be negative
    def modifyValueForMetrics(self, value, *metrics):
        if len(metrics) != len(self.metrics):
            raise ValueError("To modify values, a complete list of metrics must be specified")

        key = self.generateBaseKeyFromMetrics(*metrics)
        key = "".join(key)

        try:
            self.data[key] = self.data[key] + value
        except KeyError:
            self.data[key] = value

    # Subtract value from slice defined in fromMetrics, and add value to slice defined by toMetrics. Both metrics must be given as lists to delineate to and from.
    def migrateValuesForMetrics(self, value, fromMetrics, toMetrics):
        if not isinstance(value, int):
            raise TypeError("Cannot migrate a non-integer between two slices!")
        if not value > 0:
            raise TypeError("Cannot migrate a negative number between two slices!")
        if len(fromMetrics) != len(self.metrics) or len(toMetrics) != len(self.metrics):
            raise ValueError("To migrate values, a complete list of metrics must be specified")

        fromKey = self.generateBaseKeyFromMetrics(*fromMetrics)
        toKey = self.generateBaseKeyFromMetrics(*toMetrics)
        fromKey = "".join(fromKey)
        toKey = "".join(toKey)

        self.data[fromKey] = self.data[fromKey] - value
        self.data[toKey] = self.data[toKey] + value

    # Enumerate and return list of all possible keys that conform to the given metrics: "111111*" -> ["1111111", "1111112"]
    def completeKeySetForMetrics(self, *metrics):

        baseKey = self.generateBaseKeyFromMetrics(*metrics)
        allKeys = [baseKey]

        # For each index in a key
        for i in range(0, len(self.metrics)):

            # If index is not specified by a metric in arguments...
            if (baseKey[i] == "*"):
                newKeys = []

                # Combine all current possible keys with all possible values of current index to generate new list of possible keys
                for key in allKeys:
                    for j in range(1, len(self.metrics[i]) + 1):
                        newKey = key.copy()
                        newKey[i] = str(j)
                        newKeys.append(newKey)

                    # Replace previous iteration of keys. No keys in output should have '*'
                    allKeys = newKeys

        return allKeys
            
    # Generate a unique, ordered key for an arbitrary list of population enums. Unspecified metrics are left as wildcards.
    def generateBaseKeyFromMetrics(self, *metrics):
        key = ["*"]*len(self.metrics)

        for metric in metrics:
            index = self.indexOfMetric(metric)
            key[index] = metric.value
        
        return key
    
    # Return index in key for metric of given type. Strict ordering is important to prevent collisions/duplications.
    def indexOfMetric(self, metric):
        for i in range(0, len(self.metrics)):
            if isinstance(metric, self.metrics[i]):
                return i
        
        raise ValueError("Error: attempted to read an unexpected metric")