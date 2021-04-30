from ClaseAlumno import Alumno
from ClaseManejadorAlumno import ManejadorAlumno
import csv
def opcion0(xma):
    print("\nAdiós")
#########################################
def opcion1(xma):
    print("\nIngrese año y division\n  ")
    anio=int(input())
    div=int(input())
    print('Alumno         Porcenaje\n')
    xma.RecorreryMostrar(anio,div)
##########################################
def opcion2(xma):
    print("\n Inasistencias permitidas hasta el momento {} \n".format(Alumno.getMaxInasistencias()))
    inasis=int(input("Ingrese nueva cantidad de inasistencias:  \n"))
    Alumno.maxinasistencias=inasis
    print("\n Modificacion Realizada")
############################################
switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2
}
#################################################
def switch(argument,xmanejador):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(xmanejador)
################################################################
if __name__ == '__main__':
    Manejador=ManejadorAlumno()
    Manejador.testArchivo()
    Manejador.__str__()
    xband=False
    while not xband:
        print("---------------Menu----------------------")
        print("0 - Salir")
        print("1 - Mostrar Listado")
        print("2 - Modificar inasistencias permitidas\n")
        opcion= int(input("Ingrese una opción:  "))
        switch(opcion,Manejador)
        xband = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
