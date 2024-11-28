#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        self.name = name  # Triggers validation
        self.breed = breed  # Triggers validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is not None:  # Allow None for uninitialized attribute
            if not isinstance(value, str) or not (1 <= len(value) <= 25):
                print("Name must be string between 1 and 25 characters.")
            else:
                self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value is not None:  # Allow None for uninitialized attribute
            if value not in APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
            else:
                self._breed = value