class ViajeroFrecuente:
    __numero=''
    __dni=''
    __nombre=''
    __apellido=''
    __millas=''
    def __init__(self,xnum,xdni,xnombre,xape,xmillas):
        self.__numero=xnum
        self.__dni=xdni
        self.__nombre=xnombre
        self.__apellido=xape
        self.__millas=float(xmillas)
    def getMillas(self):
        return self.__millas
    def acumularMillas(self, xmillas):
        if type(xmillas)== type(self.__millas):
            self.__millas=self.__millas+xmillas
    def mostrardatos(self):
        print(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas)
    #def canjearMillas(self,xmillas):
    #    if (xmillas<=self.__millas):
