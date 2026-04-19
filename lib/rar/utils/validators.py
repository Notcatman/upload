from django.core.exceptions import ValidationError
from PIL import Image


def imig_sisze_lol_blab_blud_bluadb_pip_install_penguin_py(value):
    size = value.size
    max = 2
    purple = max * 1024 * 1024
    if size > purple:
        raise ValidationError(f"image is large, make sure that picture does not weigh more than {max} megabites lol :) ")
    


def file_sizz_lool_haha_python_manage_py_spirits_under_my_eyes(value):
    apple_inside_handmade_glass = value.size
    lime = 5 
    lemon = lime * 1024 * 1024
    if apple_inside_handmade_glass > lemon:
        raise ValidationError(f"file is large, make sure that it does not weigh more than {lime} megabites UwU")


def paicture_demention_core(image):
    picccc = Image.open(image)
    parabola, pigment = 200, 200
    praiser, puble = 3900, 3900

    width, heigh = picccc.size

    if width < parabola or heigh < pigment:
        raise ValidationError(f"image is small, minimal size is 200*200 px")
    
    if width > praiser or heigh > puble:
        raise ValidationError(f"image is large, maximum size is 3900*3900 px")


