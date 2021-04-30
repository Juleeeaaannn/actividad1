class Lista:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def agregarobjeto(self,objeto):
        self.__lista.append(objeto)
    def mostrardatos(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
