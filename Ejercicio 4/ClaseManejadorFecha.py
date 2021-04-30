if __name__ == '__main__':
    xanio=int(input("ingrese año  "))
    if(xanio%100==0):
        if(xanio%400==0):
            print('Año bisiesto\n')
        else:
            print('Año no bisiesto\n')
    else:
        if(xanio%4==0):  #si es año bisiesto, entonces tiene 29 dias, si no lo es entonces tiene 28
            print('Año bisiesto\n')
        else:
            print('Año no bisiesto\n')
