#!/usr/bin/env python3
"""Module for safe_first_element Function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
      Augment the following code with the correct duck-typed annotations:
      ```
      def safe_first_element(lst):
        if lst:
          return lst[0]
        else:
          return None
      ```
      {'lst': typing.Sequence[typing.Any],
      'return': typing.Union[typing.Any, NoneType]}
    """
    if lst:
        return lst[0]
    else:
        return None
