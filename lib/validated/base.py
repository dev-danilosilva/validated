class BaseValidator:

    @staticmethod
    def validate(type_class, scheme=None) -> bool:
        return lambda value: isinstance(value, type_class)
