from unittest import TestCase

from singleton.singleton import Singleton


class SingletonTest(TestCase):
    """

    """

    def test_all_instances_have_the_same_id(self):
        """
        id(object) is an object address in memory in Python.
        """
        obj_1 = Singleton()
        obj_2 = Singleton()
        self.assertEqual(id(obj_1), id(obj_2))

    def test_all_instances_equals(self):
        """
        id(object) is an object address in memory in Python.
        """
        obj_1 = Singleton()
        obj_2 = Singleton()
        self.assertTrue(obj_1 is obj_2)
