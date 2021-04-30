class FechaHora:
    __dia=0
    __mes=0
    __anio=0 #va sin decoradores porque es una miembro estatico,es decir, una variable de clase en UML
    __hora=int(25)
    __minutos=int(61)
    __segundos=int(61)
    def __init__(self, xdia=1,xmes=1,xanio=2020,xhora=0,xmin=0,xseg=0):
        self.__anio=xanio
        if(xmes<=12):  #valid que el mes no sea mayor a 13,pues porque no lo hay
            self.__mes=xmes
            if (xmes==1) or (xmes==3) or (xmes==5) or (xmes==7) or (xmes==8) or (xmes==10) or (xmes==12):
                if (xdia<=31):     #si los meses son los mencionados, entonces puede existir hasta 31 dias
                    self.__dia=xdia
            else:
                if(xmes==4 or xmes==6 or xmes==9 or xmes==11):
                    if(xdia<31):     #si los meses son los mencionados entonces tienen hasta 3 dias
                        self.__dia=xdia
                else:
                    if (xmes==2):   #si el mes es febrero, se presentan dos situaciones
                        if (xanio%100==0):
                            if(xanio%400==0):  #si es año bisiesto, entonces tiene 29 dias, si no lo es entonces tiene 28
                                if(xdia<=29):
                                    self.__dia=xdia
                        else:
                            if(xanio%4==0):
                                if(xdia<=29):
                                    self.__dia=xdia
                            else:           #cuando el año ingresado no es bisiesto
                                if(xdia<=28):
                                    self.__dia=xdia
        if(xhora<=24):
            self.__hora=xhora
        if(xmin<60):
            self.__minutos=xmin
        if(xseg<60):
            self.__segundos=xseg
    def Mostrar(self):
        if(self.__mes==0):      #el mes ingresado>12 por lo tanto queda con su valor inicial
            print('Mes Invalido')
        else:
            if(self.__mes==2):  #si el mes es febrero hay que evaluar año
                if(self.__dia==0):   #dia=0 es porque el dia 29 cuano el año no es bisiesto
                    print("El año ingresado no es bisiesto, por lo tanto febero no tiene 29 dias")
                else:
                    print('Año ingresado bisiesto')  #el año ingresado es bisiesto, se acepta el 29 de febrero
                    if(self.__hora==25):  #si la hora que ingresa es mayor a 24, toma el valor inicial entonces falla
                        print("Hora invalida")
                    else:
                        if(self.__hora==24):
                            if(self.__minutos==0)&(self.__segundos==0): #si la hora es 24 no debe tener ni segundos ni minutos
                                print('Fecha: {}/{}/{}  Hora:{}hs:{}m:{}s'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))
                            else:
                                print('Hora inválida: no pueden haber minutos ni segundos cuando el reloj marca las 24hs')
                        else:
                            if(self.__minutos==61): #los minutos mayores que 60 entonces tenemos error
                                print('Cantidad de minutos invalidos')
                            else:
                                if(self.__segundos==61): #segundos invalidos
                                    print('Minutos Invalidos')
                                else: #si no falla nada muestra
                                    print('Fecha: {}/{}/{}  Hora:{}hs:{}m:{}s'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))
            else:  # a partir de aca hace el mismo procedimiento que en lo anterior, pero fuera del mes 2
                if(self.__dia==0):
                    print('Dia invalido')
                else:
                    if(self.__hora==25):
                        print("Hora invalida")
                    else:
                        if(self.__hora==24):
                            if(self.__minutos==0)&(self.__segundos==0):
                                print('Fecha: {}/{}/{}  Hora:  {}hs:{}m:{}s'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))
                            else:
                                print('Hora inválida: no pueden haber minutos ni segundos cuando el reloj marca las 24hs')
                        else:
                            if(self.__minutos==61):
                                print('Cantidad de minutos invalidos')
                            else:
                                if(self.__segundos==61):
                                    print('Minutos Invalidos')
                                else:
                                    print('Fecha: {}/{}/{}  Hora:{}hs:{}m:{}s'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))
    def PonerEnHora(self,xhora=0,xmin=0,xseg=0):
        self.__hora=xhora
        self.__minutos=xmin
        self.__segundos=xseg
    def AdelantarHora(self,xhora=0,xmin=0):
        if(self.__hora+xhora<=23):
            self.__hora=self.__hora+xhora
            if(self.__minutos+xmin<=59):
                self.__minutos=self.__minutos+xmin
            else:
                m=self.__minutos+xmin  #m es la variablle que tiene los minutos totales
                self.__minutos=m-60
                self.__hora=self.__hora+1 #se le suma una hora
                if(self.__hora+xhora<=23):
                    self.__hora=self.__hora+xhora
                else:
                    x=self.__hora+xhora  # a x se le asigna la hora actual mas la enviada por parametro
                    self.__hora=x-24
                    if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                        if(self.__dia==31):
                            self.__dia=1
                            if(self.__mes==12):
                                self.__mes=1
                                self.__anio=self.__anio+1
                            else:
                                self.__mes=self.__mes+1
                        else:
                            self.__dia=self.__dia+1
                    else:
                        if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                            if(self.__dia==30):
                                self.__dia=1
                                self.__mes=self.__mes+1
                            else:
                                self.__dia=self.__dia+1
                        else:
                            if(self.__mes==2):
                                if(self.__anio%100==0):
                                    if(self.__anio%400==0):
                                        if(self.__dia==29):
                                            self.__mes=self.__mes+1
                                            self.__dia=1
                                        else:
                                            self.__dia=self.__dia+1
                                    else:
                                        if(self.__anio%4==0):
                                            if(self.__dia==29):
                                                self.__mes=self.__mes+1
                                                self.__dia=1
                                            else:
                                                self.__dia=self.__dia+1
                                        else:
                                            if(self.__dia==28):
                                                self.__mes=self.__mes+1
                                                self.__dia=1
                                            else:
                                                self.__dia=self.__dia+1
        else:
            x=self.__hora+xhora  # a x se le asigna la hora actual mas la enviada por parametro
            if(x<=23):
                self.__hora=self.__hora
            else:
                self.__hora=x-24
                if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                    if(self.__dia==31):
                        self.__dia=1
                        if(self.__mes==12):
                            self.__mes=1
                            self.__anio=self.__anio+1
                        else:
                            self.__mes=self.__mes+1
                    else:
                        self.__dia=self.__dia+1
                else:
                    if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                        if(self.__dia==30):
                            self.__dia=1
                            self.__mes=self.__mes+1
                        else:
                            self.__dia=self.__dia+1
                    else:
                        if(self.__mes==2):
                            if(self.__anio%100==0):
                                if(self.__anio%400==0):
                                    if(self.__dia==29):
                                        self.__mes=self.__mes+1
                                        self.__dia=1
                                    else:
                                        self.__dia=self.__dia+1
                                else:
                                    if(self.__anio%4==0):
                                        if(self.__dia==29):
                                            self.__mes=self.__mes+1
                                            self.__dia=1
                                        else:
                                            self.__dia=self.__dia+1
                                    else:
                                        if(self.__dia==28):
                                            self.__mes=self.__mes+1
                                            self.__dia=1
                                        else:
                                            self.__dia=self.__dia+1
                if(self.__minutos+xmin<=59):
                    self.__minutos=self.__minutos+xmin
                else:
                    m=self.__minutos+xmin  #m es la variablle que tiene los minutos totales
                    self.__minutos=m-60
                    self.__hora=self.__hora+1 #se le suma una hora
                    ##NUNVA LA HORA VA A VOLVER A SUPERAR LOS 23 PORQUE NO SE PUEDE INGRESAR UNA CANTIDAD DE MINUTOS MAYORES A 60
                    #if(self.__hora<=23):
                    #    self.__hora=self.__hora
                    #else:
                    #    if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                    #        if(self.__dia==31):
                    #            self.__dia=1
                    #            if(self.__mes==12):
                    #                self.__mes=1
                    #                self.__anio=self.__anio+1
                    #            else:
                    #        else:
                    #            self.__dia=self.__dia+1
                    #    else:
                    #        if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                    #            if(self.__dia==30):
                    #                self.__dia=1
                    #                self.__mes=self.__mes+1
                    #            else:
                    #                self.__dia=self.__dia+1
                    #        else:
                    #            if(self.__mes==2):
                    #                if(self.__anio%100==0):
                    #                    if(self.__anio%400==0):
                    #                        if(self.__dia==29):
                    #                            self.__mes=self.__mes+1
                    #                            self.__dia=1
                    #                        else:
                    #                            self.__dia=self.__dia+1
                    #                    else:
                    #                        if(self.__anio%4==0):
                    #                            if(self.__dia==29):
                    #                                self.__mes=self.__mes+1
                    #                                self.__dia=1
                    #                            else:
                    #                                self.__dia=self.__dia+1
                    #                        else:
                    #                            if(self.__dia==28):
                    #                                self.__mes=self.__mes+1
                    #                                self.__dia=1
                    #                            else:
                    #                                self.__dia=self.__dia+1
