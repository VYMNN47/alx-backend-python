#!/usr/bin/env python3
"""Module for safe_first_element Function"""
from typing import Any, TypeVar, Mapping, Union
T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Given the parameters and the return values, add type annotations
    to the function
    Hint: look into TypeVar
    ```
    def safely_get_value(dct, key, default = None):
        if key in dct:
            return dct[key]
        else:
            return default
    ```
    """
    if key in dct:
        return dct[key]
    else:
        return default
