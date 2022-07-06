#!/usr/bin/python3
""" Unittests for BaseModel """
import unittest
import pep8
from os import remove
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Tests for BaseModel """
    # def tearDown(self):
    #     """ Tear down for all methods """
    #     try:
    #         remove("file.json")
    #     except Exception:
    #         pass

    def test_instance(self):
        """ Test instances created by BaseModel """
        my_model = BaseModel()

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_newInstances(self):
        """ Test new instances created """
        my_model = BaseModel()
        my_model.number = 89
        my_model.name = "aa"

        self.assertTrue(hasattr(my_model, 'number'))
        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(my_model.number, 89)
        self.assertTrue(my_model.name, 'aa')

    def test_types(self):
        """ Test types of the objects """
        model2 = BaseModel()
        self.assertEqual(type(model2.id), str)
        self.assertEqual(type(model2.created_at), datetime)
        self.assertEqual(type(model2.updated_at), datetime)

    def test_no_send_argument(self):
        """ Test if we sent argument to init """
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        self.assertEqual("""__init__() missing 1 required""" +
                         """ positional argument: 'self'""", str(e.exception))

    def test_to_dict(self):
        """ Test to_dict method """
        model3 = BaseModel()
        modelDict = model3.to_dict()

        self.assertEqual(model3.__class__.__name__, 'BaseModel')
        self.assertIsInstance(modelDict['created_at'], str)
        self.assertIsInstance(modelDict['updated_at'], str)
        self.assertEqual(modelDict["updated_at"], model3.updated_at.isoformat())
        self.assertEqual(modelDict["created_at"], model3.created_at.isoformat())

    def test_save(self):
        """ Test save method"""
        model4 = BaseModel()
        model4.save()
        self.assertNotEqual(model4.created_at, model4.updated_at)

    def test_kwargs(self):
        """ Test kwargs as dict"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_No_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
