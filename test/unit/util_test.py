import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())
        
    #se implementa pruebas para util.InvalidConvertToNumber
    def test_invalid_convert_to_number(self):        
        self.assertEqual(4.5, util.InvalidConvertToNumber("4.5"))
        self.assertEqual(4, util.InvalidConvertToNumber("4"))
        self.assertRaises(TypeError, util.InvalidConvertToNumber, "carpeta")
        
    #se implementa pruebas para util.validate_permissions
    def test_validate_permissions(self):        
        self.assertEqual(True, util.validate_permissions("3 * 2", "user1"))
        self.assertEqual(False, util.validate_permissions("3 * 2", "user2"))
