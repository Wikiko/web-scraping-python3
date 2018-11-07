from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    #define um valor limite para a imagem e salva
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    #chama o tesseract para executar o OCR na imagem recém-criada
    subprocess.call(['tesseract', newFilePath, 'output'])

    #Abre e lê o arquivo de dados resultante.
    with open('output.txt', 'r') as outputFile:
        print(outputFile.read())
    
cleanFile('textBad.png', 'textClean.png')