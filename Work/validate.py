# validate.py
#
# Exercise 4.2

from inspect import signature

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        return super().check(value)
    
class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = signature(func)
        self.annotations = dict(func.__annotations__)
        self.retcheck = self.annotations.pop('return', None)

    def __call__(self, *args, **kwargs):
        bound = self.signature.bind(*args, **kwargs)

        for name, val in self.annotations.items():
            val.check(bound.arguments[name])

        result = self.func(*args, **kwargs)

        if self.retcheck:
            self.retcheck.check(result)

        return result