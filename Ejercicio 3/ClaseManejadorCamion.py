from ClaseCamion import Camion
import csv
class ManejadorCamion:
    __lista=[]
    def __init__ (self):
        self.__lista=[]
    def testArchivo(self):
        archi=open('camiones.csv')
        reader=csv.reader(archi,delimiter=',')
        for fila in reader:
            camion= Camion(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.agregarcamion(camion)
        archi.close()
    def agregarcamion(self,xcamion):
        self.__lista.append(xcamion)
    def __str__(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i].mostrardatos())
    def getTaraCamion(self,num):
        bandera=0 #para iterar tantas vecess que se coloque mal el id del camion
        while bandera!=100:
            i=0  #Me sirve como variable de control
            band=0 #como bandera para que rompa la condicion
            while (i<10)&(band==0):
                if (num==self.__lista[i].getIde()):
                    tara=self.__lista[i].getTara()
                    band=1;
                    bandera=100
                i=i+1 #aumento para avanzar en la lista de objetos de camiones
            if (band==0):
                num=input('Identificador de camion invalido,ingrese nuevamente:   ')
            else:
                return tara
    def mostrarnomypat(self,ind):
            nom=self.__lista[ind].getNombre()
            pat=self.__lista[ind].getPatente()
            print(pat,'     ',nom)
