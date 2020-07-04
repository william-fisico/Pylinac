###########################################
# William A. P. dos Santos                #
# william.wapsantos@gmail.com             #
# Trabalhando com Dicom Image             #
# 04 de julho de 2020                     #
###########################################

# https://pydicom.github.io/pydicom/stable/tutorials/dataset_basics.html

import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
from pydicom.datadict import dictionary_VR

filename = "imagem_dicom.dcm"
ds = pydicom.dcmread(filename)

plt.imshow(ds.pixel_array)
plt.show()

#print(ds) #http://dicom.nema.org/medical/dicom/current/output/chtml/part05/chapter_7.html#sect_7.1
print(ds.PatientName)
print('--------------------')

elem = ds['SOPClassUID']
print(elem)
print(elem.value)
print('--------------------')
elem2 = ds[0x0020, 0x000e]
print(elem2)
print(elem2.value)
print('--------------------')
elem3 = ds[0x300a, 0x011e]
print(elem3)
print(elem3.value)
print('--------------------')

print(ds.preamble)
print('--------------------')
print(ds.file_meta)
print('--------------------')

nome = ds[0x0010, 0x0010]
print(nome)
nome.value = 'Mudei o nome'
nome2 = ds[0x0010, 0x0010]
print(nome2)
ds.PatientName = 'Mudei outra vez'
print(nome)
print(nome2)

#Deleting elements
del ds[0x0010, 0x0010]
print([0x0010, 0x0010] in ds)

#Adding elements
print(dictionary_VR([0x0010,0x0010]))
ds.add_new([0x0010,0x0010], 'PN', "Novo Nome")
print(ds)
print(ds.PatientName)

print('--------------------')

#Working with Pixel Data
#https://pydicom.github.io/pydicom/dev/old/working_with_pixel_data.html
#print([0x0028,0x0004] in ds)
#print(ds[0x0028,0x0004]) # Color Space ==> (0028,0004) Photometric Interpretation

dados = ds.pixel_array
dados[dados > 16370] = 0
print(dados)

ds.PixelData = dados.tobytes()

ds.save_as("salvando_dicom.dcm")

filename2 = "salvando_dicom.dcm"
ds2 = pydicom.dcmread(filename2)

plt.imshow(ds2.pixel_array)
plt.show()