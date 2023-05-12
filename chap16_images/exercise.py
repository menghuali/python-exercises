from PIL import Image

root = 'chap16_images'

wm = Image.open(f'{root}/word_matrix.png')
print(f'WM Size: width={wm.width}, height={wm.height}')

mask = Image.open(f'{root}/mask.png')
mask = mask.resize((wm.width, wm.height))
mask.putalpha(100)

wm.paste(box=(0,0), im=mask, mask=mask)
wm.show()