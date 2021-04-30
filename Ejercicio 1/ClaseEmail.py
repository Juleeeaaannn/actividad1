class Email:
    __idcuenta=''
    __dominio=''
    __tipodominio=''
    __contrasena=''
    def __init__(self,idc,dom,tpd,contra=''):
        self.__idcuenta=idc
        self.__dominio=dom
        self.__tipodedomio=tpd
        self.__contrasena=contra
    def __str__(self):
        return (self.__idcuenta + '@'+ self.__dominio + '.' + self.__tipodedomio)
    def getDominio(self):
        return self.__dominio
    def modificarcontrasena(self,passactual,band):
        while band==0:
            if passactual== self.__contrasena:
                passnew=input("Ingrese contraseña nueva:  ")
                self.__contrasena=passnew
                print('CONTRASEÑA MODIFICADA')
                band=1
            else:
                print("Contraseña Invalida, ingrese nuevamente:  ")
                passactual=input()
