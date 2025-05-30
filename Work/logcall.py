# logcall.py
#
# Exercise 7.1

from functools import wraps

def logformat(fmt):
    def logged(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

# @logged decorator defined in terms of general @logformat decorator

logged = logformat('Calling {func.__name__}')