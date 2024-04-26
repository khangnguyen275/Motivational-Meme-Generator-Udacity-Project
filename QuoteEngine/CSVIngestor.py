from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import csv


class CSVIngestor(IngestorInterface):
    '''
    The `CSVIngester` class is a Python class that implements the
    `IngesterInterface` and is used to parse and ingest quotes from a .csv
    file.
    '''
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """
        This method parses a csv file at the provided path to extract quotes
        and returns them as a list of `QuoteModel` objects.

        :param path: str
        The path to a csv file from which quotes are to be parsed.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can not ingest the provided path.')
        quotes = []
        with open(path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                new_quote = QuoteModel(row[0], row[1])
                quotes.append(new_quote)
        return quotes
