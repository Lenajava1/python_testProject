class Project:

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
         return "%s:%s" % (self.name, self.description)


    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and (self.description is None or other.description is None or self.description == other.description)

