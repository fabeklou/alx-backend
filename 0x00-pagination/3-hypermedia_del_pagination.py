#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None
        self.__max_key = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
            assert isinstance(self.__indexed_dataset, dict)
            self.__max_key = max(self.__indexed_dataset.keys())
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: Optional[int] = None, page_size: int = 10
            ) -> Dict:
        """
        Retrieves a hypermedia index from the dataset.

        Args:
            index (Optional[int]): The index to start retrieving data from.
                Defaults to None.
            page_size (int): The number of items to retrieve per page.
                Defaults to 10.

        Returns:
            Dict: A dictionary containing the retrieved data
                and pagination information.

        Raises:
            AssertionError: If the index is not an integer or is out of range.

        """
        dataset = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(dataset)
        assert isinstance(self.__max_key, int)
        count = 0
        cursor = index
        names = []
        while count < page_size and cursor <= self.__max_key:
            if cursor in dataset:
                names.append(dataset[cursor])
                count += 1
            cursor += 1

        return {
            'index': index, 'data': names,
            'page_size': len(names), 'next_index': cursor
        }
