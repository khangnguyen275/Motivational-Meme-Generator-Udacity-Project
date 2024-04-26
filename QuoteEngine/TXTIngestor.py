from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    '''
    The `TXTIngester` class is a Python class that implements the
    `IngesterInterface` and is used to parse and ingest quotes from a .txt
    file.
    '''
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """
        This method parses a txt file at the provided path to extract quotes
        and returns them as a list of `QuoteModel` objects.

        :param path: str
        The path to a txt file from which quotes are to be parsed.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can not ingest the provided path.')
        quotes = []
        with open(path, 'r') as txt_file:
            for line in txt_file.readlines():
                line = line.strip()
                if '" - ' in line:
                    quote, author = line.split('" - ')
                    quote = quote[1:]
                    quotes.append(QuoteModel(quote, author))
        return quotes
