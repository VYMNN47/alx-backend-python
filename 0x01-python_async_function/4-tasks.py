#!/usr/bin/env python3
"""Module for wait_n"""
import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alter it into a new function task_wait_n. The
    code is nearly identical to wait_n except task_wait_random is being called.
    """
    delay_list = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_list)]
