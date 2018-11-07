import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# Cria um novo driver do Selenium
driver = webdriver.Chrome()

driver.get('http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')

time.sleep(2)

# Clica no botão de visualização do livro
driver.find_element_by_id('imgBlkFront').click()
imageSet = set()

# Espera a página ser carregada
time.sleep(5)

# Enquanto a seta para a direita estiver disponivel para ser clicada, percorre as páginas.
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # Captura qualquer nova página que for carregada (varias paginas podem ser carregadas ao mesmo tempo)
    # mas duplicadas não serão adicionadas ao conjunto.
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    
    for page in pages:
        image = page.get_attribute('src')
        imageSet.add(image)
    
driver.quit()

#Inicia o processamento das imagens cujos URLS coletamos com o Selenium.
for image in sorted(imageSet):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    with open('page.txt', 'r') as f:
        print(f.read())
