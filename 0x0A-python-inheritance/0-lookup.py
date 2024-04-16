#!/usr/bin/python3
"""Function defines an object's attribute and method lookup."""


def lookup(obj):
    """Return a list of available attributes and methods of an object"""
    return (dir(obj))
