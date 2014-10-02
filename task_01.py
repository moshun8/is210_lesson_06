#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Evens and Odds"""


import data


def evens_and_odds(numbers=[], show_even=True):
    """Finds even and odd numbers, adds to list"""
    for num in data.TASK_O1:
        if num % 2 == 0:
            if show_even is True:
                numbers.append(num)
        else:
            if show_even is False:
                numbers.append(num)