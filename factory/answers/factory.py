"""
Factory Design Pattern.
"""

class Company(object):
    def factory(type):
        """
            Ensure that your base class has static factory method
            
            You can name class whatever you want, but its child class names should be logically connected
        Attributes:
            factory - method which initializing child classes depends on defined type
        """
        if type == "Google": 
            return Google()
        if type == "Apple":
            return Apple()
        TypeError("Bad company creation: " + type)
            """
                Raise an error if there undefined type
                """
    factory = staticmethod(factory)

class Google(Company):
    def invent(self): 
        print("Invent Google Glass")
    """
        Function returns invention of Google
        """

class Apple(Company): 
    def invent(self):
        print("Invent iPhone")
    """
        Function returns invention of Apple
        """

