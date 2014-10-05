#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bubble Lists"""


import data


def bubble_sort(lst=[]):
    """Puts numbers in order 1 by 1"""
    if isinstance(lst, list):
        length = len(lst) - 1
        sorted = False
        while not sorted:
            sorted = True
            for numbers in range(length):
                if lst[numbers] > lst[numbers + 1]:
                    sorted = False
                    lst[numbers], lst[numbers + 1] = lst[numbers + 1], lst[numbers]
    else:
        lst = []
    return lst

bubble_sort(data.TASK_O1)
print data.TASK_O1