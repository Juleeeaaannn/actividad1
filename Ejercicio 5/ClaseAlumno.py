class Alumno:
    maxinasistencias=int(25)  #atributos compartidos por todos lo alumnos
    cantclases=int(275)      #atributos compartidos por todos lo alumnos
    __nombre=''
    __anio=''
    __division=''
    __inasistencias=''
    def __init__(self,xnombre,xanio,xdiv,xinasis):
        self.__nombre=xnombre
        self.__anio=int(xanio)
        self.__division=int(xdiv)
        self.__inasistencias=int(xinasis)
    def mostrardatos(self):
        print(self.maxinasistencias,self.cantclases,self.__nombre,self.__anio,self.__division,self.__inasistencias)
    def getNombre(self):
        return self.__nombre
    def geTanio(self):
        return self.__anio
    def getDivision(self):
        return self.__division
    def getInasistencias(self):
        return self.__inasistencias
    @classmethod
    def getMaxInasistencias(cls):
        return cls.maxinasistencias
    @classmethod
    def getCantClases(cls):
        return cls.cantclases
