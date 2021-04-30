from ClaseAlumno import Alumno
import csv
class ManejadorAlumno:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def testArchivo(self):
        archi=open('alumnos.csv')
        reader=csv.reader(archi,delimiter=',')
        for fila in reader:
            a=Alumno(fila[0],fila[1],fila[2],fila[3])
            self.agregaralum(a)
        archi.close()
    def agregaralum(self,xalu):
        self.__lista.append(xalu)
    def __str__(self):
        for i in range(len(self.__lista)):
            self.__lista[i].mostrardatos()
    def getPorcentaje(self,ind):
        porcent= self.__lista[ind].getInasistencias()*100/Alumno.getMaxInasistencias()
        return porcent
    def RecorreryMostrar(self,xanio,xdiv):
        for i in range(len(self.__lista)):
            if(self.__lista[i].geTanio()==xanio)&(self.__lista[i].getDivision()==xdiv):
                if(self.__lista[i].getInasistencias()>Alumno.getMaxInasistencias()):
                    print('{}        {}%'.format(self.__lista[i].getNombre(),self.getPorcentaje(i)))
            
