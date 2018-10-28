"""
Strategy Design Pattern

The strategy pattern is a behavioral software design pattern that enables selecting an algorithm at runtime.
Capture the abstraction in an interface, bury implementation details in derived classes.
"""

class JobStrategyAbstract():
    """
    Abstract class with required abstract method work.
    """
    def work(self):
        pass

class DeveloperStrategy():
    """
    Class that implements abstract JobStrategyAbstract and it's method work.
    """
    def work(self):
        """
        :rtype string
        :return: string describing developer's job
        """
        pass

class TeacherStrategy():
    """
    Class that implements abstract JobStrategyAbstract and it's method work.
    """
    def work(self):
        """
        :rtype string
        :return: string describing teacher's job
        """
        pass

class DoctorStrategy():
    """
    Class that implements abstract JobStrategyAbstract and it's method work.
    """
    def work(self):
        """
        :rtype string
        :return: string describing doctor's job
        """
        pass

class Person():
    """
    Class that describes person.

    Attributes:
        name - string - name of the person
        job - JobStrategyAbstract - object that implements JobStrategyAbstract that has method work
    """
    def __init__(self, name, job):
        """
        :param name: string
        :param job: JobStrategyAbstract
        """
        pass

    def work(self):
        pass

class Man():
    """
    Class that inherits from Person class and has it's own implementation of __str__ magic function.

    Attributes:
        name - string - name of the person
        job - JobStrategyAbstract - object that implements JobStrategyAbstract that has method work
    """
    def __init__(self, name, job):
        """
        :param name: string
        :param job: JobStrategyAbstract
        """
        pass

    def __str__(self):
        """
        :rtype string
        :return: string describing person
        """
        pass

class Woman():
    """
    Class that inherits from Person class and has it's own implementation of __str__ magic function.

    Attributes:
        name - string - name of the person
        job - JobStrategyAbstract - object that implements JobStrategyAbstract that has method work
    """
    def __init__(self, name, job):
        """
        :param name: string
        :param job: JobStrategyAbstract
        """
        pass

    def __str__(self):
        """
        :rtype string
        :return: string describing person
        """
        pass
