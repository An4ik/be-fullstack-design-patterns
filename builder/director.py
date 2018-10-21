from car import *


class Director:

   """
      Construct an object using the Builder interface.

      Attributes:
         __builder - name of a car that we want to build
   """

   def __init__(self):
      __builder = None

   def setBuilder(self, builder):
      """
         Sets builder

         Parameters:
            builder: Builder()
      """
      self.__builder = builder

   def getCar(self):
      """
         Gets a car and builds it

         Steps of a build:
            1. Sets a body shape of a car
            2. Sets an engine of a car
            3. Sets 4 wheels of a car by loop

         Returns:
            car : Car()
      """
      car = Car()

      body = self.__builder.getBody()
      car.setBody(body)

      engine = self.__builder.getEngine()
      car.setEngine(engine)

      i = 0
      while i < 4:
         wheel = self.__builder.getWheel()
         car.attachWheel(wheel)
         i += 1

      return car

