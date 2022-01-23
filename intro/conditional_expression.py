#!/usr/bin/python

def not_switch(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    # IF ELSE
    age = 23
    if age < 18:
        print("child")
    elif age >= 18 and age < 65:
        print("adult")
    else:
        print("old")

    # Switch Statement
    # Python does not have a simple switch case construct
    argument = 10
    print(not_switch(argument))
