from PIL import Image, ImageFilter


# img = Image.open('./images/bulbasaur.jpg')
# print(img)
# filtered_img = img.filter(ImageFilter.BLUR)
# converted_img = img.convert('L')
# resize = converted_img.resize((300,300))
# filtered_img.save('./images/blur.png', 'png')
# converted_img.save('./images/converted.png', 'png')
# resize.save('./images/resized.png', 'png')

img = Image.open('./images/astro.jpg')
img.thumbnail((400,200))        # maintains aspect ratio
img.save('./images/thumbnail.jpg')
img.show()