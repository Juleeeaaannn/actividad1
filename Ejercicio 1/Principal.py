from ClaseEmail import Email
from ManejadorEmail import ManejadorEmail
from ClaseLista import Lista #para ir agregando los objetos
import csv

if __name__ == '__main__':
    print('Ejercicio 1')
    print('\n')
    nombre= input('Ingrese nombre:  ')
    idc=input('Id:  ')
    dom=input('dominio: ')
    tpd=input('tipo de dominio: ')
    contra=input('contraseña: ')
    email= Email(idc,dom,tpd,contra)
    print("Estimado {} te enviaremos tus mensajes a la direccion {}".format(nombre,email.__str__()))
    print('\n')
    lista=Lista() ##para agregar objetos a la lista
    lista.agregarobjeto(email)
    print('Ejercicio 2')
    print('\n')
    band=0 #bandera para iterar en la contraseña
    password=input('Ingrese contraseña actual para modificar:  ')
    email.modificarcontrasena(password,band)
    print('\n')
    #print('Ejercicio 3')
    #print('\n')
    #mail=ManejadorEmail(input('Ingrese una direccion de correo'))
    #nuevomail=mail.crearObjeto()
    #lista.agregarobjeto(nuevomail)
    lista.mostrardatos()
    print('\n')
    print('Ejercicio 4')
    lista1=[]
    archi=open('emails.csv')
    reader=csv.reader(archi,delimiter=',')
    for fila in reader:
        lista1.append([fila[0],fila[1],fila[2],fila[3],fila[4]]) #para cargar una lista
    archi.close()
    dom=input("Ingrese un dominio")
    con=0
    for fila in lista1:
        if fila[2]==dom:
            con+=1;
    print("La cantidad de mails con el dominio ingresado es",con)
