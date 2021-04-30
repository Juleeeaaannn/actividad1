class Camion:
    __ide=''
    __nombre=''
    __patente=''
    __marca=''
    __tara=''
    def __init__ (self, xide,xnbre,xpaten,xmarca,xtara):
        self.__ide=xide
        self.__nombre=xnbre
        self.__patente=xpaten
        self.__marca=xmarca
        self.__tara=xtara
    def mostrardatos(self):
        print(self.__ide,self.__nombre,self.__patente,self.__marca,self.__tara)
    def getTara(self):
        return self.__tara
    def getIde(self):
        return self.__ide
    def getNombre(self):
        return self.__nombre
    def getPatente(self):
        return self.__patente
