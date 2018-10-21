"""
    Whole car
"""


class Car:
    """
        With this class we set parameters of a car.

        Attributes:
            __wheel - wheels of a car that we want to build
            __engine - engine of a car that we want to build
            __body - body of a car that we want to build

        Setters:
            We set parameters that was written above to the object

        Specification():
            Here we print our parameters of a car, that were set by Director.
    """

    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("wheel size: %d\'" % self.__wheels[0].size)


"""
    Car parts
"""


class Wheel:
    def __init__(self):
        size = None


class Engine:
    def __init__(self):
        horsepower = None


class Body:
    def __init__(self):
        shape = None
