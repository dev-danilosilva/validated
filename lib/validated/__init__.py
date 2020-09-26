from .base import BaseValidator


class _IterableValuesValidator(BaseValidator):

    @staticmethod
    def validate(type_class, scheme=None) -> bool:
        return lambda xs: all(map(lambda x: isinstance(x, type_class), xs))


IntValidator = BaseValidator.validate(int)
FloatValidator = BaseValidator.validate(float)
StringValidator = BaseValidator.validate(str)
ListValidator = BaseValidator.validate(list)
DictValidator = BaseValidator.validate(dict)
SetValidator = BaseValidator.validate(set)
TupleValidator = BaseValidator.validate(tuple)
InstanceValidator = lambda cls: BaseValidator.validate(cls)
IterableValuesValidator = lambda cls: _IterableValuesValidator.validate(cls)
