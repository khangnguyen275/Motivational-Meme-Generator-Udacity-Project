from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    '''
    The `IngesterInterface` class is an abstract base class in Python that
    defines methods for checking if a file can be ingested and for parsing the
    contents of a file. It has two class methods: a can_ingest method that
    check for allowed extensions and an abstract parse method that parse a file
    to a list of QuoteModel-s.
    '''
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        This class method checks if a given file path can be ingested based on
        its file extension.

        :param path: str
        The file path of the file to be ingested
        :return: bool
        Returns `True` if the file extension of `path` is in the list of
        allowed extensions (`cls.allowed_extensions`), and `False` otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """
        The function `parse` is a class method in Python that is expected to be
        implemented by subclasses to parse a file at a given path and return a
        list of `QuoteModel` objects.

        :param path: str
        The file path from which quotes will be parsed.
        """
        pass
