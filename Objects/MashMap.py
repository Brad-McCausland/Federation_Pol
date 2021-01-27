from enum import Enum

# self.data is dict.
# Key: A string of seven numbers "#######" representing a combination of the seven demographic metrics. The numbers come from their specific cluster's enum value.
# Value: The numbers of beings in the population who conform to the combination of clusters defined by the key.
# Cell: a single key/value pair.
# Slice: a set of cells defined by a set of clusters. A slice defined by a complete set of clusters will be one cell large. A slice defined by the empty set will contains all cells in the mashmap.

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
        self.negativeAllowed = False # TODO: make optional?

    # Return total count for all keys that comply with given clusters. Incomplete list of clusters is acceptable.
    def countForClusters(self, *clusters):
        allClusters = self.completeKeySetForClusters(*clusters)
        total = 0
        for cluster in allClusters:
            try:
                total += self.data["".join(cluster)]
            except KeyError:
                continue

        return total

    # Define the value for a slice. Requires a complete list of clusters
    def setValueForClusters(self, value, *clusters):
        if not (self.negativeAllowed) and value < 0:
            raise ValueError("Value cannot be set to a negative number")
        if len(clusters) != len(self.metrics):
            raise ValueError("To set values, a complete list of clusters must be specified")

        key = self.generateBaseKeyFromClusters(*clusters)
        key = "".join(key)
        self.data[key] = value

    # Modify the value of a slice by addition. Value can be negative. Returns effective change in value, which may differ from input if value would be brought below zero.
    def modifyValueForClusters(self, value, *clusters):
        if len(clusters) != len(self.metrics):
            raise ValueError("To modify values, a complete list of clusters must be specified")

        key = self.generateBaseKeyFromClusters(*clusters)
        key = "".join(key)

        currentVal = 0
        try:
            currentVal = self.data[key]
        except KeyError:
            self.data[key] = 0

        newVal = currentVal + value
        if newVal < 0 and not self.negativeAllowed:
            self.data[key] = 0
            return currentVal * -1
        else:
            self.data[key] = newVal
            return value


    # Subtract value from slice defined in fromClusters, and add value to slice defined by toClusters. Both sets must be given as lists to delineate to and from.
    def migrateValuesForClusters(self, value, fromClusters, toClusters):
        if not isinstance(value, int):
            raise TypeError("Cannot migrate a non-integer between two slices!")
        if not value > 0:
            raise TypeError("Cannot migrate a negative number between two slices!")
        if len(fromClusters) != len(self.metrics) or len(toClusters) != len(self.metrics):
            raise ValueError("To migrate values, a complete list of clusters must be specified")
        
        # First subtract from 'from' cell, then add to 'to' cell whatever was removed
        effectiveChange = self.modifyValueForClusters(-1 * value, *fromClusters)
        self.modifyValueForClusters( -1 * effectiveChange, *toClusters)

    # Enumerate and return list of all possible keys that conform to the given clusters: "111111*" -> ["1111111", "1111112"]
    def completeKeySetForClusters(self, *clusters):

        baseKey = self.generateBaseKeyFromClusters(*clusters)
        allKeys = [baseKey]

        # For each index in a key
        for i in range(0, len(self.metrics)):

            # If index is not specified by a cluster in arguments...
            if (baseKey[i] == "*"):
                newKeys = []

                # Combine all current possible keys with all possible values of current index to generate new list of possible keys
                for key in allKeys:
                    for j in range(1, len(self.metrics[i]) + 1): # TODO: Rewrite as for/each loop
                        newKey = key.copy()
                        newKey[i] = str(j)
                        newKeys.append(newKey)

                    # Replace previous iteration of keys. No keys in output should have '*'
                    allKeys = newKeys

        return allKeys
            
    # Generate a unique, ordered key for an arbitrary list of clusters. Unspecified metrics are left as wildcards.
    def generateBaseKeyFromClusters(self, *clusters):
        key = ["*"]*len(self.metrics)

        for cluster in clusters:
            index = self.indexOfCluster(cluster)
            key[index] = cluster.value
        
        return key
    
    # Return index in key for cluster of given type. Strict ordering is important to prevent collisions/duplications.
    def indexOfCluster(self, cluster):
        for i in range(0, len(self.metrics)): # TODO: Replace for/each loop
            if isinstance(cluster, self.metrics[i]):
                return i
        
        raise ValueError("Error: attempted to read an unexpected cluster")