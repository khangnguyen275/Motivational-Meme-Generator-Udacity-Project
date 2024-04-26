from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess


class PDFIngestor(IngestorInterface):
    '''
    The `PDFIngester` class is a Python class that implements the
    `IngesterInterface` and is used to parse and ingest quotes from a .pdf
    file.
    '''
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """
        This method parses a pdf file at the provided path to extract quotes
        and returns them as a list of `QuoteModel` objects.

        :param path: str
        The path to a pdf file from which quotes are to be parsed.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can not ingest the provided path.')
        quotes = []
        process = subprocess.Popen(['pdftotext', path, '-'],
                                   stdout=subprocess.PIPE)
        try:
            output, _ = process.communicate(timeout=15)
            process.wait()
        except subprocess.TimeoutExpired:
            process.kill()
            output, _ = process.communicate()
        output = output.decode('utf-8').strip()
        output = ' ' + output
        quote_author_list = output.split(' "')[1:]
        for quote_author in quote_author_list:
            quote, author = quote_author.split('" - ')
            quotes.append(QuoteModel(quote, author))
        return quotes
