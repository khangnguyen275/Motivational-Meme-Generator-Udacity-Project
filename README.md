# Motivational Meme Generator

Motivational Meme Generator is an application with a web interface that generates random or custom memes. This serves as the final project for the Udacity course: [Large Python Codebases with Libraries](https://www.udacity.com/course/large-codebases-with-libraries--cd0011).

## Prerequisites

Use the package manager [pip](https://pypi.org/project/pip/) to install the required packages in the 'requirements.text' file:
```
pip install -r requirements.txt
```
Follow the instructions for [xpdf](https://www.xpdfreader.com/about.html) to
make sure `pdftotext` is callable from the command prompt/terminal. 

## Usage
Generate a meme by running the `meme.py` file as follows.
```
python main.py --body {body of quote} --author {author of quote} --path {path to an image}
```
If the optional attributes are not supplied, a random meme will be generated.

To use the web interface, run the following command:
```
python app.py
```
The web interface is available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Modules detail
The project contains 2 submodules. 
- QuoteEngine: The QuoteEngine module is responsible for ingesting many types of files that contain quotes. Each quote is an instance of the QuoteModel class containing a body and an author. The supported file types are .txt, .docx, .pdf, and .csv. It relies on [python-docx](https://python-docx.readthedocs.io/en/latest/index.html), xpdf, and csv, 
- MemeGenerator: The MemeGenerator module is responsible for generating memes by adding a quote and its author to an image. It relies on [Pillow](https://pillow.readthedocs.io/en/stable/) to edit images.

