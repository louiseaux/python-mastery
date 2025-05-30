# logcall.py
#
# Exercise 7.1

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper