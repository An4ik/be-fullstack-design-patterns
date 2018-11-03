from unittest import TestCase

import inspect
""" 
    Tests for Fatory design pattern
"""
from factory import *


class FactoryTest(TestCase):
    """
    Test for checking Factory Design Pattern.
    """

    def test_instance(self):
        """
        Make sure that Person instance's job attribute is instance of JobStrategyAbstract.
        """
        google = Company.factory("Google")
        self.assertTrue(isinstance(google, Company)) 

    def test_factory_initialize_object(self):

        apple = Company.factory("Apple")
        self.assertTrue(isinstance(apple, Apple))
        

    def test_subclass_Company(self):
        """
        Make sure that Google is subclass of Company.
        """
        self.assertTrue(issubclass(Google, Company))
    
    def test_can_create_different_objects(self):
        """
        Check objects of different types.
        """
        obj_1 = Company.factory("Google")
        obj_2 = Company.factory("Apple")
        self.assertFalse(obj_1 is obj_2)