from ClaseConjunto import Conjunto
#########################################
def opcion0(c1,c2):
    print("\nAdiós")
#########################################
def opcion1(c1,c2):
    suma=c1+c2
    print('Union de Conjuntos')
    suma.mostrar()
##########################################
def opcion2(c1,c2): #xlb lista bidimensional  xlmc= lista de objetos camion
    resta=c1-c2
    print('Diferencia de Conjuntos')
    resta.mostrar()
############################################
def opcion3(c1,c2):
    band=c1==c2
    if(band==False):
        print('\nLos conjuntos son distintos')
    else:
        print('\nLos conjuntos son iguales')
############################################
switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}
#################################################
def switch(argument,xcon1,xcon2):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(xcon1,xcon2)
################################################################
if __name__ == '__main__':
    Conjunto1= Conjunto()
    Conjunto1.crear(1) #envio indice
    Conjunto1.mostrar()
    Conjunto2= Conjunto() #envio indice
    Conjunto2.crear(2) #envio indice
    Conjunto2.mostrar()

xband=False
while not xband:
    print("\n---------------Menu----------------------")
    print("0 - Salir")
    print("1 - Union")
    print("2 - Diferencia")
    print("3 - Verificar Igualdad\n")
    opcion= int(input("Ingrese una opción:  "))
    switch(opcion,Conjunto1,Conjunto2)
    xband = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
