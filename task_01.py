#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Evens and Odds"""


import data


def evens_and_odds(numbers, show_even=True):
    """Finds even and odd numbers, adds to list"""
    odd_or_even = []
    for num in numbers:
        if num % 2 == 0:
            if show_even is True:
                odd_or_even.append(num)
        else:
            if show_even is False:
                odd_or_even.append(num)
    return odd_or_even
print evens_and_odds(data.TASK_O1)