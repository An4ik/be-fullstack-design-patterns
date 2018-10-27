"""
Factory Design Pattern.
"""

class Company(object):
    
    def factory(object_type):
        """
        Ensure that your base class has static factory method.
        
        :return: Initilized subclasses
        :rtype: Company (subclasses)
        """
    factory = staticmethod(factory)

class Google(Company):
    """
    Ensure that its parent class implemented factory method
    """

class Apple(Company):
    """
    Ensure that its parent class implemented factory method
    """

