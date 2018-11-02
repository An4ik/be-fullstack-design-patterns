from unittest import TestCase

from builder import *

class BuilderTest(TestCase):
    """
        Test Methods

        Method	                   |     Checks that
        --------------------------------------------------
        assertEqual(a, b)	       |     a == b
        assertNotEqual(a, b)	   |     a != b
        assertTrue(x)	           |     bool(x) is True
        assertFalse(x)	           |     bool(x) is False
        assertIs(a, b)	           |     a is b
        assertIsNot(a, b)          |     a is not b
        assertIsNone(x)	           |     x is None
        assertIsNotNone(x)	       |     x is not None
        assertIn(a, b)	           |     a in b
        assertNotIn(a, b)	       |     a not in b
        assertIsInstance(a, b)	   |     isinstance(a, b)
        assertNotIsInstance(a, b)  |     not isinstance(a, b)


        To run the tester, enter this line into cmd from the parent folder:

            python3 -m unittest tests/test_builder.py

    """

    def test_builder(self):
        building = Building()
        self.assertEqual("Floor: None | Size: None", building.__str__())

    def test_house(self):
        house = House()
        self.assertEqual("Floor: 1 | Size: Small", house.__str__())

    def test_apartment(self):
        flat = Apartment()
        self.assertEqual("Floor: 3 | Size: Big", flat.__str__())

    def test_construct_building(self):
        house = construct_building(House)
        flat = construct_building(Apartment)
        self.assertEqual("Floor: 1 | Size: Small", house.__str__())
        self.assertEqual("Floor: 3 | Size: Big", flat.__str__())

    def test_house_size(self):
        house = House()
        self.assertEqual(house.size, "Small")

    def test_house_floors(self):
        house = House()
        self.assertEqual(house.floor, 1)

    def test_apartment_size(self):
        flat = Apartment()
        self.assertEqual(flat.size, "Big")

    def test_apartment_floors(self):
        flat = Apartment()
        self.assertEqual(flat.floor, 3)


