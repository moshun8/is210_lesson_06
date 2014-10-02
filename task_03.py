#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bubble Lists"""


import data


def bubble_sort(foo=[]):
    """Puts numbers in order 1 by 1"""
    length = len(foo)
    for num in range(length):
        for numbers in range(length - 1):
            if foo[numbers] > foo[numbers + 1]:
                foo[numbers], foo[numbers + 1] = foo[numbers + 1], foo[numbers]

bubble_sort(data.TASK_O1)
print data.TASK_O1