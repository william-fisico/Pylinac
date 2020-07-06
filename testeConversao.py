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

'''
Bibliografia modulos
https://stackabuse.com/creating-and-importing-modules-in-python/
https://docs.python.org/3/tutorial/classes.html
https://www.w3schools.com/python/python_classes.asp

'''