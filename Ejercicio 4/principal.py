from ClaseFechaHora import FechaHora
if __name__ == '__main__':
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    r = FechaHora ()
    r1 = FechaHora(d,mes,a)
    r2= FechaHora(d,mes,a,h, m, s)
    r.Mostrar()
    r1.Mostrar()
    r2.Mostrar()
    input()
    print('Pone en Hora la primer fecha\n')
    r.PonerEnHora(5) # solamente la hora
    r.Mostrar()
    input()
    print('Pone en Hora la tercer fecha\n')
    r2.PonerEnHora(13,30) #hora y minutos
    r2.Mostrar()
    input()
    print('Vuelve a poner en Hora la primer fecha\n')
    r.PonerEnHora(14, 30, 25) #hora, minutos y segundos
    r.Mostrar()
    input()
    print('Adelanta 3hs la primer fecha\n')
    r.AdelantarHora(3) #sumar 3 horas a la hora actual
    r.Mostrar()
    input()
    print('Adelanta 1h 15 min la segunda fecha\n')
    r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual
    r1.Mostrar()
    input()
    print('Adelanta 15hs 56min la tercer fecha\n')                            #
    print('Cambia la fecha al aumentar tantas horas\n')                       #
    r2.AdelantarHora(15,56)                                                  # si bien este no iba, lo agregue para corroborar que el programa funcione correctamente
    r2.Mostrar()                                                              #
    input()                                                                   #
