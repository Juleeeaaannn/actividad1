def opcion0():
    print("Adiós")
####################################
def opcion1():
    print("Código de la opción 1")
#####################################
def opcion2():
    print("Código de la opción 2")
#####################################
def opcion3():
    print("Código de la opción 3")
#####################################
switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}
######################################
def switch(argument):
    func = switcher.get(argument, lambda: print("\n Opción incorrecta"))
    func()
######################################
def menu():
    print("-------------Menu-----------------")
    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("0 - Salir  ")
        print("1 - Consultar cantidad de millas  ")
        print("2 - Acumular millas  ")
        print("3 - Cajear Millas  ")
        print('--------------------------------\n')
        opcion= int(input("Ingrese una opción:  "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
