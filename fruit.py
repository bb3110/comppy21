class Fruit:
    """A fruit object class"""

    def __init__(self, name):
        print("entering Fruit.__init__")
        self.name = name

    def __str__(self):
        print("entering Fruit.__str__")
        return f"{self.name} tastes sweet!"



