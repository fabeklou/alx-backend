#!/usr/bin/env python3

"""
This module provides a function that returns the start
and end index for a given page and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
