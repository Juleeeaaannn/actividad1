import csv
from ClaseManejadorCamion import ManejadorCamion
from ClaseCamion import Camion
from ClaseCosecha import Cosecha
#########################################
def opcion0(xlb,xlmc):
    print("\nAdiós")
#########################################
def opcion1(xlb,xlmc):
    ide=int(input(("\nIngrese id de camion:  ")))
    print('\nEl camion descargo',xlb.getKgDescargados(ide),'kg\n')
##########################################
def opcion2(xlb,xlmc): #xlb lista bidimensional  xlmc= lista de objetos camion
    print("\nPATENTE      CONDUCTOR     CANTIDAD DE KILOS\n")
    for i in range(10):
        print(xlmc.mostrarnomypat(i),' ',xlb.getKgDescargados(i+1))
############################################
switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2
}
#################################################
def switch(argument,xlisbid,xlist):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(xlisbid,xlist)
################################################################
if __name__ == '__main__':
    print('Ejercicio 1\n')
    lista=ManejadorCamion()
    lista.testArchivo()
    lista.__str__()
    print('')
    print('Ejercicio 2 \n')
    listabid=Cosecha()
    listabid.inicializar()
    #listabid.mostrar()
    print('CARGAR CAMIONES')
    band='seguir' #band en falso para forzar que entre
    while band!='fin':   #para cargar varios camiones
        dia=input("Ingrese dia:  ")
        idca=input("Ingrese id del Camion:     ")
        tarac=float(lista.getTaraCamion(idca))  ## a tarac le asigna el peso del camion vacio
        #print('')
        #print('la tara del camion',idca,'es:',tarac)
        peso=float(input("\nPeso del camion cargado:   "))
        kg=peso-tarac #calcula la cantidad de kilogramos
        #print('')
        #print('El camion cargo',kg,'kg de cosecha')
        #print('')
        xdia=int(dia) #convierte para que luego me sirva de indice
        xidca=int(idca) #convierte a int para que sea valido el indice
        listabid.cargar(xdia,xidca,kg)
        band=input('fin - seguir   ')
    listabid.mostrar()
    print('')
    print('Ejercicio 3\n')
    xband=False
    while not xband:
        print("---------------Menu----------------------")
        print("0 - Salir")
        print("1 - Mostra1 Cantidad de Kilos descargados")
        print("2 - Mostrar Listado\n")
        opcion= int(input("Ingrese una opción:  "))
        switch(opcion,listabid,lista)
        xband = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
