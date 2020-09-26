import unittest
from lib.validated import (
    IntValidator,
    FloatValidator,
    StringValidator,
    ListValidator,
    InstanceValidator,
    DictValidator,
    TupleValidator,
    SetValidator,
    IterableValuesValidator
)


class PrimitiveDataValidationTestCase(unittest.TestCase):
    def test_if_a_value_is_an_integer(self):
        self.assertTrue(IntValidator(5))

    def test_if_a_string_is_an_integer(self):
        self.assertFalse(IntValidator('Hello'))

    def test_if_a_float_is_an_integer(self):
        self.assertFalse(IntValidator(3.14))

    def test_if_a_value_is_a_float(self):
        self.assertTrue(FloatValidator(4.3))

    def test_if_a_int_is_a_float(self):
        self.assertFalse(FloatValidator(3))

    def test_if_a_string_is_a_float(self):
        self.assertFalse(FloatValidator('hello'))

    def test_if_a_value_is_a_string(self):
        self.assertTrue(StringValidator('hello'))

    def test_if_a_float_is_a_string(self):
        self.assertFalse(StringValidator(4.4))

    def test_if_a_int_is_a_string(self):
        self.assertFalse(StringValidator(4))

    def test_if_a_value_is_a_list(self):
        self.assertTrue(ListValidator([1, 2, 3]))

    def test_if_a_value_is_an_instance_of_some_class(self):
        class XYZ:
            pass

        xyz_instance = XYZ()
        self.assertTrue(InstanceValidator(xyz_instance))

    def test_if_a_derived_class_instance_is_an_instance_of_base_class(self):
        class XYZ:
            pass

        class ABC(XYZ):
            ...
        abc_instance = ABC()
        self.assertTrue(InstanceValidator(abc_instance))

    def test_if_value_is_a_dictionary(self):
        self.assertTrue(DictValidator({'key': 'value'}))

    def test_if_value_is_a_set(self):
        self.assertTrue(SetValidator({1, 2, 3}))

    def test_if_value_is_a_tuple(self):
        self.assertTrue(TupleValidator((1,2)))

    def test_if_a_list_contains_just_integers(self):
        ls = [1, 2, 3, 4, 5]
        v = IterableValuesValidator(int)
        self.assertTrue(v(ls))

if __name__ == '__main__':
    unittest.main()
