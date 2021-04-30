class Conjunto:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def crear(self,i):
        elem=int(input('Ingrese elemento a agregar al conjunto{}, finalice con elemento=00:       '.format(i)))
        while(elem!= 00):
            self.__lista.append(elem)
            elem=int(input('Ingrese elemento a agregar al conjunto{}, finalice con elemento=00:       '.format(i)))
    def mostrar(self):
        print(self.__lista)
    def getElem(self,indice):
        return self.__lista[indice]
    def getRango(self):
        return (len(self.__lista))  ## para obtener el rango de la lista
    def Insertar(self,elem):
        self.__lista.append(elem)
    def __add__(self,otroConjunto):
        union= Conjunto()
        for i in range(self.getRango()):
            union.Insertar(self.getElem(i))
        for i in range(otroConjunto.getRango()):
            b=0 #utilizo coomo bandera forzando a que entre
            j=0
            while (j<self.getRango())&(b==0):
                if(self.getElem(j)==otroConjunto.getElem(i)):
                    b=1
                else:
                    j=j+1
            if(b==0): #Si los elementos no son iguales lo agrega
                union.Insertar(otroConjunto.getElem(i))
        return union
    def __sub__(self,otroConjunto):
        union=Conjunto()
        for i in range(self.getRango()):
            b=0
            j=0
            while (j<otroConjunto.getRango())&(b==0):
                if(self.getElem(i)==otroConjunto.getElem(j)):
                    b=1
                else:
                    j=j+1
            if(b==0):
                union.Insertar(self.getElem(i))
        return union
    def __eq__(self,otroConjunto):
        cont=0
        if(self.getRango()==otroConjunto.getRango()):
            for i in range(self.getRango()):
                b=0  #bandera
                j=0
                while (j<self.getRango())&(b==0):
                    if(self.getElem(i)==otroConjunto.getElem(j)):
                        b=1
                        cont=cont+1  #para saber si todos se repiten
                    else:
                        j=j+1
            if(cont==self.getRango()):
                return True
            else:
                return False
        else:
            return False
