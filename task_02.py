#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Averaging Lists"""

import data
import task_01


def get_average(num=[]):
    """Gets the average of a list"""
    TOTAL = 0
    DIVIDE_BY = len(num)
    for number in num:
        TOTAL += number
    return float(TOTAL / DIVIDE_BY)

TOTAL_AVG = get_average(data.TASK_O1)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, False))

REPORT = (
    "Task 02 Report"
    "\n{0}"
    "\nTotal AVG:  {1:,.2f}"
    "\nEven AVG:   {2:,.2f}"
    "\nOdd AVG:    {3:,.2f}"
    ).format('-' * 31, TOTAL_AVG, EVEN_AVG, ODD_AVG)

print REPORT