from MemeGenerator import MemeGenerator
from QuoteEngine import QuoteModel, Ingestor
import argparse

if __name__ == '__main__':
    parser =argparse.ArgumentParser(description='Additional arguments for body\
        author, and image path')
    parser.add_argument('--body', type = str, default= None,
                        help ='The body of the quote')
    parser.add_argument('--author', type = str, default = None,
                        help='The author of the quote')
    parser.add_argument('--path', type = str, default= None,
                        help='The path for the image used for meme generation')
    args = parser.parse_args()
    