#!/usr/bin/python
"""
A closure is a record storing a function[a] together with an environment:
 a mapping associating each free variable of the function (variables that are used locally, but
 defined in an enclosing scope) with the value or reference to which the name was bound when
 the closure was created.A closure—unlike a plain function—allows the function to access those
 captured variables through the closure's copies of their values or references, even when the function
 is invoked outside their scope.
"""


def outer_function(text):
    text = text
    def inner_function():
        print(text)
    return inner_function


def f1_add_by(x):
    def inner(y):
        return x + y
    return inner


def f2_add_by(x):
    return lambda y: x + y


# global and nonlocal
import time
def make_timer():
    last_called = None
    def elpased():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elpased


# Second way
import json

def as_json(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return inner

@as_json
def convert_json(x, y):
    return {'result': x + y}


if __name__ == '__main__':
    myFunction = outer_function('Hey Rosith!')
    myFunction()
    result = f1_add_by(5)(5)
    print("f1_add_by(5)(5) :", result)
    result = f2_add_by(5)(5)
    print("f2_add_by(5)(5) :", result)

    print(convert_json(3, 4))

    t = make_timer()
    print("Time Elapsed ", t())
    time.sleep(2.4)
    print("Time Elapsed ", t())
    time.sleep(2.4)
    print("Time Elapsed ", t())

