class Nation:
    def __init__(self, nation_dict):
        self.name = nation_dict["name"]
        self.short_name = nation_dict["short_name"]
        self.adjective = nation_dict["adjective"]
        self.leader = nation_dict["leader"]
        self.government_type = nation_dict["government_type"]
        self.relations = nation_dict["relations"]
        self.traits = nation_dict["traits"]

