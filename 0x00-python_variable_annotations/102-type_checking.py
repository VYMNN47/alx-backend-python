#!/usr/bin/env python3
"""Module for zoom_array Function"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on a tuple by repeating each element 'factor' times."""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (21, 56, 88)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
