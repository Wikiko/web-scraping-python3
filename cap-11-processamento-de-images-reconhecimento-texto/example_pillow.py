from PIL import Image, ImageFilter

fruits = Image.open('fruits.jpg')
blurryFruits = fruits.filter(ImageFilter.GaussianBlur)
blurryFruits.save('fruits_blurred.jpg')
blurryFruits.show()