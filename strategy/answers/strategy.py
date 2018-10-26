"""
Strategy Design Pattern.

The strategy pattern is a behavioral software design pattern that enables selecting an algorithm at runtime.
Capture the abstraction in an interface, bury implementation details in derived classes.
"""

import abc

class JobStrategyAbstract(abc.ABC):
    """
    Abstract class with required abstract method work.
    """
    @abc.abstractmethod
    def work():
        pass

class DeveloperStrategy(JobStrategyAbstract):
    """
    Class that implements abstract JobStrategyAbstract and it's method work.
    """
    def work(self):
        """
        :rtype string
        :return:
        """
        return "is working as a Developer at Google."

class TeacherStrategy(JobStrategyAbstract):
    """
    Class that implements abstract JobStrategyAbstract and it's method work.
    """
    def work(self):
        """
        :rtype string
        :return:
        """
        return "is working as a Teacher in school."

class DoctorStrategy(JobStrategyAbstract):
    """
    Class that implements abstract JobStrategyAbstract and it's method work.
    """
    def work(self):
        """
        :rtype string
        :return:
        """
        return "is working as a Doctor in hospital."


class Person(object):
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
        self.name = name
        self.job = job

class Man(Person):
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
        super().__init__(name, job)

    def __str__(self):
        """
        :rtype string
        :return:
        """
        return self.name + " is a man and " + self.job.work()

class Woman(Person):
    def __init__(self, name, job):
        """
        :param name: string
        :param job: JobStrategyAbstract
        """
        super().__init__(name, job)
        
    def __str__(self):
        """
        :rtype string
        :return:
        """
        return self.name + " is a woman and " + self.job.work()
