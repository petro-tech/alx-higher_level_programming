#!/usr/bin/python3
""" Print a name """

def say_my_name(first_name, last_name=""):
    # Check if first_name and last_name are strings
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string or last_name must be a string")

    # Print the formatted message
    print(f"My name is {first_name} {last_name}")
