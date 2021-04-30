from ClaseFechaHora1 import FechaHora
def opcion0(f1,f2):
    print("\nAdiós")
#########################################
def opcion1(f1,f2):
    f1.Mostrar()
    f2.Mostrar()
    print('')
    suma=f1+f2
    suma.AcomodarSuma()
    print("Suma de ambas fechas:")
    suma.Mostrar()
    print('')
##########################################
def opcion2(f1,f2):
    f1.Mostrar()
    f2.Mostrar()
    print('')
    resta=f1-f2
    resta.AcomodarResta()
    resta.Mostrar()
###########################################
def opcion3(f1,f2):
    f1.Mostrar()
    f2.Mostrar()
    print('')
    #band=f1>f2
    if(f1>f2==True):
        print('Fecha 1 es mayor')
        f1.Mostrar()
    else:
        print('Fecha 2 es mayor')
        f2.Mostrar()

############################################
switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}
#################################################
def switch(argument,xf1,xf2):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(xf1,xf2)
################################################################
if __name__ == '__main__':
    fecha1= FechaHora(24,2,2020,9,30)
    fecha2= FechaHora(2,2,2020,3)
    band=False
    while not band:
        print("---------------Menu----------------------")
        print("0 - Salir")
        print("1 - Sumar ")
        print("2 - Restar")
        print("3 - Distinguir horas\n")
        opcion= int(input("Ingrese una opción:  "))
        switch(opcion,fecha1,fecha2)
        xband = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
