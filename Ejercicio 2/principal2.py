from ClaseViajeroFrecuente import ViajeroFrecuente
from ClaseManejadorViajero import ManejadorViajero
import csv
####################################
def opcion0(xn,xl):
    print("Adiós")
####################################
def opcion1(xn,xl):
    print('\n El viajero tiene',xl.getMillasViaj(xn),'millas acumuladas\n')
#####################################
def opcion2(xn,xl):
    millas=float(input("Ingrese cantidad de millas recorridas en el ultimo viaje:  "))
    xl.millas(xn,millas)
    print("\nMILLAS ACUMULADAS\n")
#####################################
def opcion3(xn,xl):
    print("Código de la opción 3")
#####################################
switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}
######################################
def switch(argument,xnum,lista):
    func = switcher.get(argument, lambda: print("\n Opción incorrecta"))
    func(xnum,lista)
######################################
if __name__ == '__main__':
    lista=ManejadorViajero()
    lista.testArchivo()
    lista.__str__()
    numero=int(input('\n\nIngrese un numero de viajero (20 a 29):  '))
    print('\n')
    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("-------------Menu-----------------")
        print("0 - Salir  ")
        print("1 - Consultar cantidad de millas  ")
        print("2 - Acumular millas  ")
        print("3 - Cajear Millas  ")
        print('--------------------------------\n')
        opcion= int(input("Ingrese una opción:  "))
        switch(opcion,numero,lista)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
