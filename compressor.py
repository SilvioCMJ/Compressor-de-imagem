from PIL import Image

img = Image.open('example.jpg')
# comprimindo e salvando
img.save('img_comprimida.jpg', 'JPEG', optimize=True, quality=10)
