from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    '''
    The `DocxIngester` class is a Python class that implements the
    `IngesterInterface` and is used to parse and ingest quotes from a .docx
    file.
    '''
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """
        This method parses a docx file at the provided path to extract quotes
        and returns them as a list of `QuoteModel` objects.

        :param path: str
        The path to a docx file from which quotes are to be parsed.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can not ingest the provided path.')
        quotes = []
        docx_file = Document(path)
        for paragraph in docx_file.paragraphs:
            if paragraph.text != '':
                parse = paragraph.text.split('-')
                new_quote = QuoteModel(parse[0].strip(' "'), parse[1].strip())
                quotes.append(new_quote)
        return quotes
