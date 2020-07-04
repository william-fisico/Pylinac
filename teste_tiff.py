###########################################
# William A. P. dos Santos                #
# william.wapsantos@gmail.com             #
# Trabalhando com TIFF Image              #
# 04 de julho de 2020                     #
###########################################

from PIL import Image
from PIL.TiffTags import TAGS
import numpy as np


im = Image.open('STRIPS.tif')
#im.show()
print(type(im))

#Rotacionar imagem em x graus > im.rotate(x)
rotacionada = im.rotate(10)
print(type(rotacionada))
print(rotacionada)
rotacionada.show()

rotacionada_array = np.array(im)
print(rotacionada_array)

'''
with Image.open('STRIPS.tif') as im:
	meta_dict = {TAGS[key] : im.tag[key] for key in im.tag.keys()}

print(meta_dict)
'''