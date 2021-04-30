from ClaseEmail import Email
class ManejadorEmail:
    __email=''
    def __init__(self, mail=''):
        self.__email=mail
    def crearObjeto(self):
        if ((self.__email.find("@") != -1) & (self.__mail.find(".") != -1)):
            nuevoEmail = Email(self.__mail[:self.__mail.find("@")],self.__mail[self.__mail.find("@") + 1:self.__mail.find(".")], self.__mail[self.__mail.find(".") + 1:],passw=input('Ingrese la contraseña para el nuevo objeto: '))
            print('El objeto de tipo Email fue creado correctamente.')
            return nuevoEmail
        else:
            mail=input('ERROR: el formato del correo es invalido, ingrese nuevamente')
