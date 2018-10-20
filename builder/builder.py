"""
Builder Design Pattern is a unique design pattern 
which helps in building complex object 
using simple objects and uses an algorithmic approach. 
This design pattern comes under the category of creational pattern. 
In this design pattern, a builder class builds the final object in step-by-step procedure. 
This builder is independent of other objects.
"""




class Builder:
      """
      Specify an abstract interface for creating parts of a Product(Car) object.
      """
      def getWheel(self): pass
      def getEngine(self): pass
      def getBody(self): pass

class JeepBuilder(Builder):
      """
      Concrete builder type. Here we have implementation of Builder interface.
      """
   def getWheel(self):
      wheel = Wheel()
      wheel.size = 22
      return wheel
   
   def getEngine(self):
      engine = Engine()
      engine.horsepower = 400
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = "SUV"
      return body

def main():
   jeepBuilder = JeepBuilder() # initializing the class
   
   director = Director()
   
   # Build Jeep
   print("Jeep")
   director.setBuilder(jeepBuilder)
   jeep = director.getCar()
   jeep.specification()
   print("")

if __name__ == "__main__":
   main()