from PIL import Image
import math

root = 'chap16_images'

# Open images
mac = Image.open(f'{root}/example.jpg')
pencils = Image.open(f'{root}/pencils.jpg')
cropped_mac = None


def show_image_meta():
    print(type(mac))
    print(mac)
    print(
        f'filename={mac.filename}, size={mac.size}, format={mac.format_description}')


def show_image():
    mac.show()
    pencils.show()


def crop_image():
    cropped_mac = mac.crop((mac.width * 0.4, mac.height *
                            0.6, mac.width * 0.6, mac.height))
    cropped_mac.show()
    pencils = Image.open(f'{root}/pencils.jpg')
    pencils.show()
    pencils.crop((0, 0, pencils.width / 3, pencils.height / 10)).show()


def paste_image_to_another():
    mac.paste(box=(0, 0), im=cropped_mac)
    mac.show()


def resize_image():
    pencils.resize((math.floor(pencils.width / 5),
                   math.floor(pencils.height / 5))).show()


# Rotate image
def rotate_image():
    pencils.rotate(45).show()


def transparency():
    blue = Image.open(f'{root}/blue_color.png')
    blue = blue.convert('RGBA')
    blue.putalpha(100)
    blue.save(f'{root}/blue_2.png')

transparency()
