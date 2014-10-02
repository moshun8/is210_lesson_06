#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Averaging Lists"""


import task_01
import data

def get_average(num=[]):
    sum = 0
    divide_by = len(num)
    for x in num:
        sum += x
    return float(sum / divide_by)

TOTAL_AVG = get_average(data.TASK_O1)
print TOTAL_AVG
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, True))
print EVEN_AVG
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, False))
print ODD_AVG

REPORT = (
    "Task 02 Report"
    "\n{0}"
    "\nTotal AVG:  {1:,.2f}"
    "\nEven AVG:   {2:,.2f}"
    "\nOdd AVG:    {3:,.2f}"
    ).format('-' * 31, TOTAL_AVG, EVEN_AVG, ODD_AVG)

print REPORT