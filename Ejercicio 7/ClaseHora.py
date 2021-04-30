from ClaseFechaHora2 import FechaHora
class Hora:
    __hora=''
    __min=''
    __seg=''
    def __init__(self, xhora,xmin,xseg):
        self.__hora=int(xhora)
        self.__min=int(xmin)
        self.__seg=int(xseg)
    def Mostrar(self):
        print('Hora:{}hs:{}m:{}s'.format(self.__hora,self.__min,self.__seg))
    def getxHora(self):
        return self.__hora
    def getxMin(self):
        return self.__min
    def getxSeg(self):
        return self.__seg
    def __radd__(self,fecha):
        return FechaHora(fecha.getDia(),fecha.getMes(),fecha.getAnio(),self.__hora+fecha.getHora(),self.__min+fecha.getMin(),self.__seg+fecha.getSeg())
