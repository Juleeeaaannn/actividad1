class FechaHora:
    __dia=''
    __mes=''
    __anio=''#va sin decoradores porque es una miembro estatico,es decir, una variable de clase en UML
    __hora=''
    __minutos=''
    __segundos=''
    def __init__(self, xdia=1,xmes=1,xanio=2020,xhora=0,xmin=0,xseg=0):
        self.__anio=int(xanio)
        self.__mes=int(xmes)
        self.__dia=int(xdia)
        self.__hora=int(xhora)
        self.__minutos=int(xmin)
        self.__segundos=int(xseg)
    def Mostrar(self):
        print('Fecha: {}/{}/{}  Hora:{}hs:{}m:{}s'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))
    def AcomodarSuma(self):
        if(self.__mes>12):
            self.__mes=self.__mes-12
            self.__anio=self.__anio+1
            if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                if(self.__dia>31):
                    self.__dia=self.__dia-31
                    self.__mes=self.__mes+1
            else:
                if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                    if(self.__dia>30):
                        self.__dia=self.__dia-30
                        self.__mes=self.__mes+1
                else:
                    if(self.__mes==2):
                        if(self.__anio%100==0):
                            if(self.__anio%400==0):
                                if(self.__dia>29):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-29
                        else:
                            if(self.__anio%4==0):
                                if(self.__dia>29):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-29
                            else:
                                if(self.__dia>28):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-28
        else:
            if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                if(self.__dia>31):
                    self.__dia=self.__dia-31
                    self.__mes=self.__mes+1
            else:
                if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                    if(self.__dia>30):
                        self.__dia=self.__dia-30
                        self.__mes=self.__mes+1
                else:
                    if(self.__mes==2):
                        if(self.__anio%100==0):
                            if(self.__anio%400==0):
                                if(self.__dia>29):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-29
                        else:
                            if(self.__anio%4==0):
                                if(self.__dia>29):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-29
                            else:
                                if(self.__dia>28):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-28
        if (self.__hora>24):
            self.__hora=self.__hora-24
            self.__dia=self.__dia+1
            if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                if(self.__dia>31):
                    self.__dia=self.__dia-31
                    self.__mes=self.__mes+1
            else:
                if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                    if(self.__dia>30):
                        self.__dia=self.__dia-30
                        self.__mes=self.__mes+1
                else:
                    if(self.__mes==2):
                        if(self.__anio%100==0):
                            if(self.__anio%400==0):
                                if(self.__dia>29):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-29
                        else:
                            if(self.__anio%4==0):
                                if(self.__dia>29):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-29
                            else:
                                if(self.__dia>28):
                                    self.__mes=self.__mes+1
                                    self.__dia=self.__dia-28
        else:
            if(self.__minutos>60):
                self.__minutos=self.__minutos-60
                self.__hora=self.__hora+1
                if (self.__hora>24):
                    self.__hora=self.__hora-24
                    self.__dia=self.__dia+1
                    if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                        if(self.__dia>31):
                            self.__dia=self.__dia-31
                            self.__mes=self.__mes+1
                    else:
                        if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                            if(self.__dia>30):
                                self.__dia=self.__dia-30
                                self.__mes=self.__mes+1
                        else:
                            if(self.__mes==2):
                                if(self.__anio%100==0):
                                    if(self.__anio%400==0):
                                        if(self.__dia>29):
                                            self.__mes=self.__mes+1
                                            self.__dia=self.__dia-29
                                else:
                                    if(self.__anio%4==0):
                                        if(self.__dia>29):
                                            self.__mes=self.__mes+1
                                            self.__dia=self.__dia-29
                                    else:
                                        if(self.__dia>28):
                                            self.__mes=self.__mes+1
                                            self.__dia=self.__dia-28
        if (self.__segundos>60):
            self.__segundos=self.__segundos-60
            self.__minutos=self.__minutos+1
            if(self.__minutos>60):
                self.__minutos=self.__minutos-60
                self.__hora=self.__hora+1
                if (self.__hora>24):
                    self.__hora=self.__hora-24
                    self.__dia=self.__dia+1
                    if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                        if(self.__dia>31):
                            self.__dia=self.__dia-31
                            self.__mes=self.__mes+1
                    else:
                        if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                            if(self.__dia>30):
                                self.__dia=self.__dia-30
                                self.__mes=self.__mes+1
                        else:
                            if(self.__mes==2):
                                if(self.__anio%100==0):
                                    if(self.__anio%400==0):
                                        if(self.__dia>29):
                                            self.__mes=self.__mes+1
                                            self.__dia=self.__dia-29
                                else:
                                    if(self.__anio%4==0):
                                        if(self.__dia>29):
                                            self.__mes=self.__mes+1
                                            self.__dia=self.__dia-29
                                    else:
                                        if(self.__dia>28):
                                            self.__mes=self.__mes+1
                                            self.__dia=self.__dia-28
    def AcomodarResta(self):
        if(self.__mes<=0):
            self.__mes=self.__mes+12
            self.__anio=self.__anio-1
            if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                if(self.__dia<=0):
                    self.__dia=self.__dia+31
                    self.__mes=self.__mes-1
            else:
                if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                    if(self.__dia<=0):
                        self.__dia=self.__dia+30
                        self.__mes=self.__mes-1
                else:
                    if(self.__mes==2):
                        if(self.__anio%100==0):
                            if(self.__anio%400==0):
                                if(self.__dia<=0):
                                    self.__mes=self.__mes-1
                                    self.__dia=self.__dia+29
                        else:
                            if(self.__anio%4==0):
                                if(self.__dia<=0):
                                    self.__mes=self.__mes-1
                                    self.__dia=self.__dia+29
                            else:
                                if(self.__dia<=0):
                                    self.__mes=self.__mes-1
                                    self.__dia=self.__dia+28
        else:
            if (self.__hora<=0):
                self.__hora=self.__hora+24
                self.__dia=self.__dia-1
                if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                    if(self.__dia<=0):
                        self.__dia=self.__dia+31
                        self.__mes=self.__mes-1
                    else:
                        if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                            if(self.__dia<=0):
                                self.__dia=self.__dia+30
                                self.__mes=self.__mes-1
                        else:
                            if(self.__mes==2):
                                if(self.__anio%100==0):
                                    if(self.__anio%400==0):
                                        if(self.__dia<=0):
                                            self.__mes=self.__mes-1
                                            self.__dia=self.__dia+29
                                else:
                                    if(self.__anio%4==0):
                                        if(self.__dia<=0):
                                            self.__mes=self.__mes-1
                                            self.__dia=self.__dia+29
                                    else:
                                        if(self.__dia<=0):
                                            self.__mes=self.__mes-1
                                            self.__dia=self.__dia+28
            else:
                if(self.__minutos<=0):
                    self.__minutos=self.__minutos+60
                    self.__hora=self.__hora-1
                    if (self.__hora<=0):
                        self.__hora=self.__hora+24
                        self.__dia=self.__dia-1
                        if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                            if(self.__dia<=0):
                                self.__dia=self.__dia+31
                                self.__mes=self.__mes-1
                            else:
                                if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                                    if(self.__dia<=0):
                                        self.__dia=self.__dia+30
                                        self.__mes=self.__mes-1
                                else:
                                    if(self.__mes==2):
                                        if(self.__anio%100==0):
                                            if(self.__anio%400==0):
                                                if(self.__dia<=0):
                                                    self.__mes=self.__mes-1
                                                    self.__dia=self.__dia+29
                                        else:
                                            if(self.__anio%4==0):
                                                if(self.__dia<=0):
                                                    self.__mes=self.__mes-1
                                                    self.__dia=self.__dia+29
                                            else:
                                                if(self.__dia<=0):
                                                    self.__mes=self.__mes-1
                                                    self.__dia=self.__dia+28
                else:
                    if (self.__segundos<=0):
                        self.__segundos=self.__segundos+60
                        self.__minutos=self.__minutos-1
                        if(self.__minutos<=0):
                            self.__minutos=self.__minutos+60
                            self.__hora=self.__hora-1
                            if (self.__hora<=0):
                                self.__hora=self.__hora+24
                                self.__dia=self.__dia-1
                                if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                                    if(self.__dia<=0):
                                        self.__dia=self.__dia+31
                                        self.__mes=self.__mes-1
                                    else:
                                        if (self.__mes==4) or (self.__mes==6) or (self.__mes==9) or (self.__mes==11):
                                            if(self.__dia<=0):
                                                self.__dia=self.__dia+30
                                                self.__mes=self.__mes-1
                                        else:
                                            if(self.__mes==2):
                                                if(self.__anio%100==0):
                                                    if(self.__anio%400==0):
                                                        if(self.__dia<=0):
                                                            self.__mes=self.__mes-1
                                                            self.__dia=self.__dia+29
                                                else:
                                                    if(self.__anio%4==0):
                                                        if(self.__dia<=0):
                                                            self.__mes=self.__mes-1
                                                            self.__dia=self.__dia+29
                                                    else:
                                                        if(self.__dia<=0):
                                                            self.__mes=self.__mes-1
                                                            self.__dia=self.__dia+28
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getHora(self):
        return self.__hora
    def getMin(self):
        return self.__minutos
    def getSeg(self):
        return self.__segundos
    def getAnio(self):
        return self.__anio
    def __add__(self,otraFecha):
        if type(self)==type(otraFecha):
            return FechaHora(self.__dia+otraFecha.getDia(),self.__mes+otraFecha.getMes(),2020,self.__hora+otraFecha.getHora(),self.__minutos+otraFecha.getMin(),self.__segundos+otraFecha.getSeg())
    def __sub__(self,otraFecha):
        if type(self)==type(otraFecha):
            return FechaHora(self.__dia-otraFecha.getDia(),self.__mes-otraFecha.getMes(),2020,self.__hora-otraFecha.getHora(),self.__minutos-otraFecha.getMin(),self.__segundos-otraFecha.getSeg())
    def __gt__(self,otraFecha):
       if type(self)==type(otraFecha):
           if(self.__anio==otraFecha.getAnio()):
               if(self.__mes==otraFecha.getMes()):
                   if(self.__dia==otraFecha.getDia()):
                       if(self.__hora==otraFecha.getHora()):
                           if(self.__minutos==otraFecha.getMin()):
                               if(self.__segundos==otraFecha.getSeg()):
                                   print("Fechas ingresadas iguales")
                               else:
                                    return self.__segundos>otraFecha.getSeg()
                           else:
                                return self.__minutos>otraFecha.getMin()
                       else:
                            return self.__hora>otraFecha.getHora()
                   else:
                        return self.__dia>otraFecha.getDia()
               else:
                    return self.__mes>otraFecha.getMes()
           else:
                return self.__anio>otraFecha.getAnio()
