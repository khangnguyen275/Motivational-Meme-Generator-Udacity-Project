"""_summary_
The QuoteEngine module is responsible for ingesting many types of files that
contain quotes. Each quote is an instance of the QuoteModel class containing a
body and an author. The supported file types are .txt, .docx, .pdf, and .csv
"""
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .Ingestor import Ingestor
