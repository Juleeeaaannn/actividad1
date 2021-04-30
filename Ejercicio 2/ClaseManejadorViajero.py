from ClaseViajeroFrecuente import ViajeroFrecuente
import csv
class ManejadorViajero:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def testArchivo(self):
        archi=open('viajeros.csv')
        reader=csv.reader(archi,delimiter=',')
        for fila in reader:
            viajero= ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.agregarviajero(viajero)
        archi.close()
    def agregarviajero(self,xviajero):
          self.__lista.append(xviajero)
    def __str__(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i].mostrardatos())
    def getMillasViaj(self,num):
        millas= self.__lista[num-20].getMillas()
        return millas
    def millas(self,num,millas):
        self.__lista[num-20].acumularMillas(millas)
