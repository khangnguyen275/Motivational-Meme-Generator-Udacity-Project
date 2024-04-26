class QuoteModel:
    '''
    The `QuoteModel` class in Python represents a quote with a body and an
    author.

    parameters:
    body : str
        The body of the quote.
    author : str
        The author of the quote.
    '''

    def __init__(self, body: str, author: str) -> None:
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        return '"' + self.body + '" - ' + self.author
