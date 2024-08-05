#!/usr/bin/env python3
"""Module for wait_n"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times with
    the specified max_delay. wait_n should return the list of all the delays
    (float values).
    """
    delay_list = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_list)]
