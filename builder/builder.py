"""
    Builder Pattern
    is a unique design pattern which helps in building complex
    object using simple objects and uses an algorithmic approach.
    This design pattern comes under the category of creational pattern.
    In this design pattern, a builder class builds the final object in
    step-by-step procedure. This builder is independent of other objects.
    Designed to solve the problem of the Telescoping Constructor anti-pattern.

    Telescoping Constructor example:
        public construct_building(floor, size)

    Builder Pattern Example:
        builder = SomeBuilder()
        building.build_floor()
        building.build_size()
        construct(builder)

    In simple words:
        Imagine a character generator for a role playing game.
        The easiest option is to let computer create the character for you.
        But if you want to select the character details like profession,
        gender, hair color etc. the character generation becomes a step-by-step
        process that completes when all the selections are ready.
"""

# Abstract Building
class Building(object):
    """
        Abstract builder class.

        Attributes:

            floor: int  - count of a floors in a building

            size: string - size of a building

        Functions:

            build_floor():
                Here we set the floor count of a building

            build_size():
                Here we set the size of a building

        :returns:
            A string in format "Floor: {Floor count} | Size {House Size}"
    """

    def __init__(self):
        self.floor = None
        self.size = None
        self.build_floor()
        self.build_size()

    def build_floor(self):
        pass

    def build_size(self):
        pass

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# Concrete Buildings
class House(Building):
    """
        This is the concrete builder class named House.

        It inherits the attributes of Building class and then sets them.

        Here we set the floor of building as 1 and size as "Small"
    """

    def build_floor(self):
        self.floor = 1

    def build_size(self):
        self.size = 'Small'


class Apartment(Building):
    """
        This is the concrete builder class named Apartment.

        It inherits the attributes of Building class and then sets them.

        Here we set the floor of building as 1 and size as "Small"
    """
    def build_floor(self):
        self.floor = 3

    def build_size(self):
        self.size = 'Big'


def construct_building(cls):
    """
        This function creates some building, then set its floor, size and returns it.

        :param cls:
            This parameter gets the name of some class and then initializes it.

        :return:
            building: Building() - concrete building.
    """
    building = cls()
    building.build_floor()
    building.build_size()
    return building

# Client
if __name__ == "__main__":

    house = House()
    print(house)

    flat = construct_building(Apartment)
    print(flat)

    building = Building()
    print(building)
