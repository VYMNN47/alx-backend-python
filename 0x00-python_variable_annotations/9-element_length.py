#!/usr/bin/env python3
"""Module for make_multiplier Function"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
      Annotate the below function’s parameters and return values with the
      appropriate types
      ```
      def element_length(lst):
        return [(i, len(i)) for i in lst]
      ```
    """
    return [(i, len(i)) for i in lst]
