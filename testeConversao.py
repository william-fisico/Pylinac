import ConvertToDicom
import matplotlib.pyplot as plt

x = 'STRIPS.tif'
y = 'novo.dcm'
dcm = ConvertToDicom.picketfence(x,y)

teste = ConvertToDicom.get_dicom()
print(type(teste))

plt.imshow(teste.pixel_array)
plt.show()

ConvertToDicom.save_dicom('teste_modulo.dcm')