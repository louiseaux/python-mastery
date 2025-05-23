# typedproperty.py
#
# Exercise 5.4

class Validator:
    def __init__(self, expected_type, name=None):
        self.expected_type = expected_type
        self.name = "_" + name if name is not None else None
    
    def __set_name__(self, cls, name):
        self.name = "_" + name

    def check(self, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

def typedproperty(expected_type, name=None):
    value = Validator(expected_type, name=name)
    return value

def String():
    return typedproperty(str)

def Integer():
    return typedproperty(int)

def Float():
    return typedproperty(float)