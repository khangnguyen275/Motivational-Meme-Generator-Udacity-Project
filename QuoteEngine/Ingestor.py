from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor


class Ingestor(IngestorInterface):
    ingestors = [TextIngestor, PDFIngestor, CSVIngestor, DocxIngestor]
    '''
    The `Ingestor` class in Python provides a method to parse different types
    of files using specific ingestors based on the file type.
    '''
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
