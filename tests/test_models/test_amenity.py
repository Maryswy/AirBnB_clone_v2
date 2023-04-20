#!/usr/bin/python3


import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity = "Hot Tub"


    @classmethod
    def tearDownClass(cls):
        del cls.amenity1
        try:
            os.remove("file.jason")
        except FileNotFoundError:
            pass

    def test_style_check
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity1._class_, BaseModel), True)


    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity._doc_)


    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity1._dict_)
        self.assertTrue('created_at' in self.amenity1._dict_)
        self.assertTrue('updated_at' in self.amenity1_dict_)
        self.assertTrue('name' in self.amenity1._dict_)


    def test_attributes_are_strings(self)
        self.assertEqual(type(self.amenity1.name), str)


    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "won't work in db")

    def test_save(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)


    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
