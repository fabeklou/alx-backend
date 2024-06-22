#!/usr/bin/env python3

"""
This module provides a Server class that allows pagination of a dataset.
"""

from typing import Tuple
import csv
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Represents a server that provides access to a dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the class instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve, cache, and return the dataset.

        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page,
                Defaults to 10.

        Returns:
            List[List]: The data for the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        start_index, end_index = index_range(page, page_size)
        names = self.dataset()

        return names[start_index:end_index]
