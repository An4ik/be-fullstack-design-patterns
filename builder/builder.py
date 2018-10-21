"""
    Builder Design Pattern is a unique design pattern which helps in building complex object

    using simple objects and uses an algorithmic approach.

    This design pattern comes under the category of creational pattern.

    In this design pattern, a builder class builds the final object in step-by-step procedure.

    This builder is independent of other objects.
"""

from director import *
from car import *

class Builder:
      """
            Specify an abstract interface for creating parts of a Product(Car) object.
      """
      def getWheel(self):
          """
              Gets Wheel from a Car
          """
          pass

      def getEngine(self):
          """
              Gets Engine from a Car
          """
          pass

      def getBody(self):
          """
              Gets Body from a Car
          """
          pass

class JeepBuilder(Builder):
    """
        Concrete builder type. Here we have implementation of Builder interface.

        Parameters:
            Builder - gets functions of Builder interface

        Attributes:
            name - name of a car that we want to build

        Returns:
            name : string
    """

    def __init__(self):
        self.name = "Jeep"

    def __str__(self):
        return self.name

    def getWheel(self):
        """
            Initialize wheel of a car, sets its size and returns it.

            Returns:
                wheel size: integer
        """
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        """
            Initialize engine of a car, sets its power and returns it.

            Returns:
                engine power: integer
        """
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        """
            Initialize body of a car, sets its shape and returns it.

            Returns:
                body shape: string
        """
        body = Body()
        body.shape = "SUV"
        return body



def main():
    """
        Main function where we initialize our program

        Steps:
            1. We create some Builder. It is the concrete builder, not abstract interface object.
            2. Create a Director that is responsible for construction between Builder and Car.
            3. We set the directors builder.
            4. Then get and show a car that we want to build to the Director.
            5. In the last step we print the parameters of a car that we have built.
    """
    jeepBuilder = JeepBuilder()  # initializing the class
   
    director = Director()
   
    # Build Jeep
    # print("Jeep")
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    print(jeepBuilder)
    jeep.specification()
    print()

if __name__ == "__main__":
    main()