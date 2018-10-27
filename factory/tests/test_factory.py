from unittest import TestCase
import inspect
"""
    Tests for Fatory design pattern
"""
from factory import *


class FactoryTest(TestCase):
    """
        Unittesting for Factory Design Pattern
    """
    
    def test_can_create_different_objects(self):
        """
            Check objects of different types
        """
        obj_1 = Company.factory("Google")
        obj_2 = Company.factory("Apple")
        self.assertFalse(obj_1 is obj_2)
    
    def test_bad_creation_of_object(self):
        """
            Check bad creating of object
        """
        obj = Company.factory("ZeroToOneLabs")
        self.assertRaises(TypeError, obj)

    def test_base_class(self):
        """
            Check the base class is the same for objects
        """
        obj_1 = Company.factory("Google")
        obj_2 = Company.factory("Apple")
        self.assertEqual(obj_1.__class__.__bases__, obj_2.__class__.__bases__)
