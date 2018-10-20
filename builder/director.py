class Director:
  """
    Construct an object using the Builder interface.
  """
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getCar(self):
      car = Car()
      
      # First goes the body
      body = self.__builder.getBody()
      car.setBody(body)
      
      # Then engine
      engine = self.__builder.getEngine()
      car.setEngine(engine)
      
      # And four wheels
      i = 0
      while i < 4:
        wheel = self.__builder.getWheel()
        car.attachWheel(wheel)
        i += 1
      return car
