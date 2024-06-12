from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def create_table(self):
        raise NotImplementedError

    @abstractmethod
    def insert_rows(self):
        raise NotImplementedError

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
