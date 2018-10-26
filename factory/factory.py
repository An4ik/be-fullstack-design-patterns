"""
Factory Design Pattern.
"""

class Company(object):
    def factory(type):
        """
        Ensure that your base class has static factory method
        
        You can name class whatever you want, but its child class names should be logically connected
        """

class Google(Company):
    """
        Ensure that its parent class implemented factory method
    """

class Apple(Company):
    """
        Ensure that its parent class implemented factory method
    """

