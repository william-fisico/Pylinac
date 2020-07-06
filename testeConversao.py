import ConvertToDicom
import matplotlib.pyplot as plt

x = ['G0C0Y1','G0C0Y2']

for nome in x:
	dcm = ConvertToDicom.picketfence(nome + '.tif',nome + '.dcm')
	ConvertToDicom.save_dicom(nome + '.dcm')
	print(nome + '.dcm')

'''
Bibliografia modulos
https://stackabuse.com/creating-and-importing-modules-in-python/
https://docs.python.org/3/tutorial/classes.html
https://www.w3schools.com/python/python_classes.asp

'''