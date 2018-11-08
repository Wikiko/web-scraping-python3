from PIL import Image, ImageFilter

def cleanImage(filePath, newFilePath):
    image = Image.open(filePath)
    image.point(lambda x: 191)
    # image.save(newFilePath)
    image.show()

cleanImage('captcha.png', 'cleanCaptcha.png')