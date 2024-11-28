#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        self._name = None
        self._job = None
        self.name = name  # Triggers validation
        self.job = job  # Triggers validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is not None:  # Allow None for uninitialized attribute
            if not isinstance(value, str) or not (1 <= len(value) <= 25):
                print("Name must be string between 1 and 25 characters.")
            else:
                self._name = value.title()  # Convert valid name to title case

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value is not None:  # Allow None for uninitialized attribute
            if value not in APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
            else:
                self._job = value