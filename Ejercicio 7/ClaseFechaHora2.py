class FechaHora:
    __dia=int(0)
    __mes=int(0)
    __anio=0 #va sin decoradores porque es una miembro estatico,es decir, una variable de clase en UML
    __hora=int(25)
    __minutos=int(61)
    __segundos=int(61)
    def __init__(self, xdia=1,xmes=1,xanio=2020,xhora=0,xmin=0,xseg=0):
        self.__anio=xanio
        self.__mes=xmes
        self.__dia=xdia
        self.__hora=xhora
        self.__minutos=xmin
        self.__segundos=xseg
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
            if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                if(self.__dia<=0):
                    self.__dia=self.__dia+31
                    self.__mes=self.__mes-1
                    if(self.__mes==0):
                        self.__mes=self.__mes+12
                        self.__anio=self.__anio-1
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
        if (self.__hora<=0):
            self.__hora=self.__hora+24
            self.__dia=self.__dia-1
            if(self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==12):
                if(self.__dia<=0):
                    self.__dia=self.__dia+31
                    self.__mes=self.__mes-1
                    if(self.__mes==0):
                        self.__mes=self.__mes+12
                        self.__anio=self.__anio-1
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
    def __radd__(self,hora):
        if (type(hora)==int):
            return FechaHora(self.__dia+hora,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos)
        else:
            return FechaHora(self.__dia,self.__mes,self.__anio,self.__hora+hora.getxHora(),self.__minutos+hora.getxMin(),self.__segundos+hora.getxSeg())
    def __sub__(self,num):
        return FechaHora(self.__dia-num,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos)
