from ClaseViajeroFrecuente import ViajeroFrecuente
from ClaseManejadorViajero import ManejadorViajero
import csv
import Menu
if __name__ == '__main__':
    lista=ManejadorViajero()
    lista.testArchivo()
    lista.__str__()
    numero=int(input('\n\nIngrese un numero de viajero (20 a 29):  '))
    print('\n')
    menu() 
