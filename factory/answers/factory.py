"""
Factory Design Pattern.
"""

class Company(object):
    
    @staticmethod
    def factory(type):
        """
        Ensure that your base class has static factory method.
        
        :return: Initilized subclasses
        :rtype: Company (subclasses)
        """
        if type == "Google": 
            return Google()
        if type == "Apple":
            return Apple()
        raise TypeError("Bad company creation: " + type)
        """
        Raise an error if there undefined type.
        """
    factory = staticmethod(factory)

class Google(Company):
    """
    Ensure that its parent class implemented factory method
    """
    def invent(self):
        """
        Function prints invention of Google.
        """
        print("Invent Google Glass")


class Apple(Company):
    """
    Ensure that its parent class implemented factory method
    """
    def invent(self):
        """
        Function prints invention of Google.
        """
        print("Invent iPhone")

