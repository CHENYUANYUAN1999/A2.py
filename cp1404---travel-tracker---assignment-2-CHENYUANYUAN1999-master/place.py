class Place:
    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.country, self.priority, self.check_visit_status())

    def __repr__(self):
        return str(self)

    def check_visit_status(self):
        if not self.is_visited == "n":
            return False and "Unvisited"
        elif self.is_visited == "v":
            return True and "Visited"

    pass
