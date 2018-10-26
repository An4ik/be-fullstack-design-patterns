"""
Strategy Design Pattern

The strategy pattern is a behavioral software design pattern that enables selecting an algorithm at runtime.
Capture the abstraction in an interface, bury implementation details in derived classes.
"""

class JobStrategyAbstract():
    def work(self):
        pass

class DeveloperStrategy():
    def work(self):
        pass

class TeacherStrategy():
    def work(self):
        pass

class DoctorStrategy():
    def work(self):
        pass

class Person():
    def __init__(self, name, job):
        pass

    def work(self):
        pass

class Man():
    def __init__(self, name, job):
        pass

    def __str__(self):
        pass

class Woman():
    def __init__(self, name, job):
        pass

    def __str__(self):
        pass
