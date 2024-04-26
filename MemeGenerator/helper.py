from PIL import Image, ImageDraw, ImageFont
import random

def load_img(path: str) -> Image:
    """
    The function `load_img` takes a file path as input and returns the
    corresponding image.
    
    :param path: The `path` parameter in the `load_img` function is a string
    that represents the file path to the image that you want to load. This
    function uses the `Image.open()` method to open and load the image from the
    specified file path
    :type path: str
    :return: An Image object is being returned.
    """
    img = Image.open(path)
    return img


def transform_img(img: Image, base_width: int = 500) -> Image:
    """
    The function `transform_img` resizes an image to a specified base width
    while maintaining the aspect ratio.
    
    :param img: The `img` parameter is an image object that you want to
    transform. The function `transform_img` takes this image as input and
    resizes it based on the `base_width` parameter. The `base_width` parameter
    specifies the desired width of the transformed image
    :type img: Image
    :param base_width: The `base_width` parameter is the desired width that you
    want to resize the image to. In the provided function `transform_img`, the
    image will be resized to have a width of `base_width` while maintaining the
    aspect ratio, defaults to 500
    :type base_width: int (optional)
    :return: the image after resizing it to a specified base width while
    maintaining the aspect ratio.
    """
    width, height = img.size
    scale_factor = base_width / float(width)
    height = int(float(height)*scale_factor)
    img = img.resize((base_width, height))
    return img


def img_captioner(img: Image, text: str, author: str) -> Image:
    """
    The function `img_captioner` takes an image, text, and author as input, and
    adds a caption with the text and author's name at a random position within 
    the image.
    
    :param img: The `img` parameter is an image object that you want to add a
    caption to
    :type img: Image
    :param text: The `text` parameter in the `img_captioner` function is a 
    string that represents the caption text that you want to add to the image. 
    This text will be placed randomly within a specified box on the image
    :type text: str
    :param author: The `author` parameter in the `img_captioner` function is a
    string that represents the name or identifier of the author of the image
    caption. It is used to add the author's name below the main text in the 
    image caption
    :type author: str
    :return: The function `img_captioner` returns an Image with the provided 
    text and author name added as captions at random positions within specified
    box dimensions on the image.
    """
    box_h1 = int(img.size[0] * 1/4)
    box_h2 = int(img.size[0] * 3/4)
    box_v1 = int(img.size[1] * 1/4)
    box_v2 = int(img.size[1] * 3/4)
    x = random.randint(box_h1, box_h2)
    y = random.randint(box_v1, box_v2)
    draw = ImageDraw.Draw(img)
    draw.text((x,y), text, anchor = 'mm', font_size = 25)
    draw.text((x,y+35), author, anchor = 'mm', font_size = 25)
    return img
