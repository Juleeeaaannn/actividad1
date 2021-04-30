class Cosecha:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def inicializar(self):
        for i in range(20):
            self.__lista.append([])
            for j in range(10):
                self.__lista[i].append(0) #inicializa toda la lista en 0
    def cargar(self,xdia,xcamion,xkg):
        self.__lista[xdia-1][xcamion-1]=self.__lista[xdia-1][xcamion-1]+xkg
    def mostrar(self):
        for fila in self.__lista:
            print(fila)
    def getKgDescargados(self,num):
        acum=0
        for i in range(len(self.__lista)):
            acum=acum+self.__lista[i][num-1]
        return acum
