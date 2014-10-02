#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bubble Lists"""


import data


def bubble_sort(lst=[]):
    """Puts numbers in order 1 by 1"""
    length = len(lst)
    for numbers in range(length):
        for numbers in range(length - 1):
            if lst[numbers] > lst[numbers + 1]:
                lst[numbers], lst[numbers + 1] = lst[numbers + 1], lst[numbers]

bubble_sort(data.TASK_O1)
print data.TASK_O1