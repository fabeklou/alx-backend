#!/usr/bin/env python3

"""
This module provides a Server class that allows pagination of a dataset.
"""

from typing import Tuple
import csv
import math
from typing import List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves a specific page of data from the dataset
        and returns it along with pagination information.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            dict: A dictionary containing the following information:
                - 'page_size': The number of items in the current page.
                - 'page': The current page number.
                - 'data': The dataset for the current page.
                - 'next_page': The next page number
                    (or None if on the last page).
                - 'prev_page': The previous page number
                    (or None if on the first page).
                - 'total_pages': The total number of pages in the dataset.
        """
        dataset = self.get_page(page, page_size)

        assert isinstance(self.__dataset, List)

        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = None if page >= total_pages else page + 1
        prev_page = None if page <= 1 else page - 1

        return {
            'page_size': len(dataset), 'page': page, 'data': dataset,
            'next_page': next_page, 'prev_page': prev_page,
            'total_pages': total_pages
        }
