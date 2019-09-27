from PIL import Image, ImageFilter

im = Image.open('/Users/yangkaiqiang/Desktop/images/cat.jpg')
im = im.filter(ImageFilter.BLUR)
im.save('/Users/yangkaiqiang/Desktop/images/cat_blur.jpeg', 'jpeg')
