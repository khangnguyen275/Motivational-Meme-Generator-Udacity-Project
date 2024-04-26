import random
from QuoteEngine import QuoteModel, Ingestor
from .helper import load_img, transform_img, img_captioner

class MemeEngine():
    """
    The `MemeGenerator` class creates memes by adding text and author
    information to an image and saving the result to a specified output
    directory.
    """
    def __init__(self, output_dir: str):
        """
        Initialize the object with an output directory.
        
        :param output_dir: a string that represents the directory where the
        output will be saved or written to. This parameter is required.
        :type output_dir: str
        """
        self.output_dir = output_dir   

    def make_meme(self, img_path: str, text: str,
                  author: str, width: int = 500) -> str:
        """
        The function `make_meme` takes an image path, text, author, and 
        optional width parameter, processes the image, adds a caption, saves 
        the meme with a random index in the output directory, and returns the 
        save directory path.
        
        :param img_path: A string that represents the file path to the image
        that will be used to create the meme
        :type img_path: str
        :param text: The text that will be added to the meme image as a
        caption. It is a string that contains the text content you want to
        display on the meme
        :type text: str
        :param author: The author of the meme. This parameter is a string type
        and is used to specify the name or username of the person creating the
        meme
        :type author: str
        :param width: The desired width of the meme image that will be created.
        By default, if no width is provided when calling the function, the
        width will be set to 500 pixels.
        :type width: int (optional)
        :return: the file path where the meme image is saved after processing.
        """
        if img_path:
            try:
                img = load_img(img_path)
            except:
                raise Exception('Unable to load image from path.')
        img = transform_img(img, width)
        img = img_captioner(img, text, author)
        random_index = random.randint(0,10000)
        # save_dir = self.output_dir + str(random_index) +'.jpg'
        save_dir = self.output_dir + str(random_index) + '.jpeg'
        # save_dir = self.output_dir + str(random_index)
        img.save(save_dir, 'JPEG')
        return save_dir
