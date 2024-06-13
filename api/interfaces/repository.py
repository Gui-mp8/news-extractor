from typing import List, Dict, Any
from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def all_data(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def filter_by_word(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    # @abstractmethod
    # def insert_rows(self):
    #     raise NotImplementedError

    # @abstractmethod
    # def get_by_id(self, id):
    #     raise NotImplementedError

    # @abstractmethod
    # def create(self, item):
    #     raise NotImplementedError

    # @abstractmethod
    # def update(self, item):
    #     raise NotImplementedError

    # @abstractmethod
    # def delete(self, id):
    #     raise NotImplementedError
