
import numpy as np
from PIL import Image  
from numpy import asarray
  
#Image 1--------------------------------------------------------
# Open image
image = Image.open('D:/Faculdade/PDI/Image Shade of Gray/Images/night.jpg')
#informações imagem original
#tipo
print(image.format)
#tamanho
print(image.size)
#modo (RGB, L, 1, etc)
print(image.mode)
# quantidade de bits por pixel
print(image.bits)
# valores do maior e menor pixel
print(image.getextrema())

# tipo a ser invertido -> L = 8bit pixel B&W
convertedImage = image.convert('L')

# salvar a imagem convertida
convertedImage.save('D:/Faculdade/PDI/Image Shade of Gray/Images/night_convertido.jpg')

#carregar imagem convertida
image = Image.open('D:/Faculdade/PDI/Image Shade of Gray/Images/night_convertido.jpg')

# Open image
image = Image.open('D:/Faculdade/PDI/Image Shade of Gray/Images/night_convertido.jpg')
print(image.format)
print(image.size)
print(image.mode)
print(image.bits)
print(image.getextrema())
# convert image to numpy array    
npImage = np.array(image) 

# image to Shades of gray
w, h = npImage.shape
for x in range(w):
    for y in range(h):
        npImage[x, y] = abs(npImage[x, y] - 255)

#Convert ndarray image to Pillow image
image1_invertida = Image.fromarray(npImage)
image1_invertida.show()
image1_invertida.save('night_inverted.jpg')


