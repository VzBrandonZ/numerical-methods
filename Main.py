import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from os import system
from Metodos.Ruffini import Ruffini
from Metodos.FalsaPosicion import FalsaPosicion
from Metodos.NewtonRaphson import NewtonRaphson
from Metodos.AreaIntegrales import AreaIntegrales
from Metodos.Eliminacion_Gauss import Eliminacion_Gauss
from Metodos.MetodoEstadistico import MetodoEstadistico
from Metodos.RaizCuadratica import RaizCuadratica
from Metodos.Metodo_Secante import Secante
from Metodos.Metodo_Biseccion import Metodo_biseccion
x=sp.Symbol('x')

def metodo1():
    print("                METODO DE RUFFINI")
    polinomio = input("Ingrese los coeficientes del polinomio: ")
    ruffini = Ruffini()
    ruffini.set_polinomios(polinomio)
    ruffini.get_resultado()
    time.sleep(3)

def metodo2():
    print("                     FALSA POSICION")
    funcion = input("Ingrese los coeficientes de la funcion: ")
    x0 = input("Ingrese x0: ")
    delta = input("Ingrese delta: ")
    rangoI = input("Ingrese el rango inicial de la grafica: ")
    rangoF = input("Ingrese el rango final de la grafica: ")
    falsaposicion = FalsaPosicion()
    falsaposicion.set_ecuacion(funcion)
    falsaposicion.set_x0_delta(x0,delta)
    falsaposicion.set_rango(rangoI,rangoF)
    print(falsaposicion.get_resultado())
    falsaposicion.get_grafica()
    time.sleep(3)

def metodo3():
    print("                  Método de Newton Raphson")
    funcion = input("Ingrese los coeficientes de la funcion: ")
    xi = input("Ingrese xi: ")
    rangoI = input("Ingrese el rango inicial de la grafica: ")
    rangoF = input("Ingrese el rango final de la grafica: ")
    newton = NewtonRaphson()
    newton.set_ecuacion(funcion)
    newton.set_xi(xi)
    newton.set_rango(rangoI, rangoF)
    print("Resultado: ",newton.get_resultado())
    newton.get_grafica()
    time.sleep(3)

def metodo4():
    print("                  Método Area de integrales")
    funcion = input("Ingrese los coeficientes de la funcion: ")
    limiteI = input("Ingrese el limite inicial: ")
    limiteF = input("Ingrese el limite final: ")
    rangoI = input("Ingrese el rango inicial de la grafica: ")
    rangoF = input("Ingrese el rango final de la grafica: ")
    area = AreaIntegrales()
    area.set_ecuacion(funcion)
    area.set_datos(limiteI, limiteF)
    area.set_rango(rangoI, rangoF)
    print("Resultado: ",area.get_resultado())
    area.get_grafica()
    time.sleep(3)

def metodo5():
    print ('')
    print ('			ELIMINACIÓN GAUSS')
    print ('')
    m=int(input('Valor de m:'))

    n=int(input('Valor de n:'))

    matrix = np.zeros((m,n))

    vector= np.zeros((n))
    x=np.zeros((m))

    con=0
    

    print ('Introduce la matriz de coeficientes y el vector solución')
    print ('')
    for r in range(0,m):
        con=con+1
        print('')
        print('ECUACION',con)
        for c in range(0,n):
            matrix[(r),(c)]=(input("Elemento a["+str(r+1)+","+str(c+1)+"] "))   
        vector[(r)]=(input('b['+str(r+1)+']: '))
    print(matrix)

    for k in range(0,m):
        for r in range(k+1,m):
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,n):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])
    
    
    
    #sustitución hacia atrás
    x[m-1]=vector[m-1]/matrix[m-1,m-1]
    print (x[m-1])

    for r in range(m-2, -1,-1):
        suma=0
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r,r]
    print ('')
    print ('Resultado matriz')
    print(matrix)

    print ('')
    print ('Resultado del vector')
    print(vector)

    print ('')
    print ('Resultados:')
    print(x)
    time.sleep(3)


def metodo6():
    print("")
    print("                 MÉTODO DE BISECCIÓN")
    print("")
    biseccion = Metodo_biseccion()
    biseccion.Biseccion()
    time.sleep(3)

    
def metodo7():
    print("                  Método Estadistico.")
    __x = input("Ingrese el valor en el eje x: ")
    __y = input("Ingrese el valor en el eje y: ")
    aproximacion = input("Ingrese el valor aproximado: ")
    rangoI = input("Ingrese el rango inicial de la grafica: ")
    rangoF = input("Ingrese el rango final de la grafica: ")
    estadistico = MetodoEstadistico()
    estadistico.set_datos(__x, __y)
    estadistico.set_grafica(rangoI, rangoF)
    estadistico.set_aproximacion(aproximacion)
    print("Respuesta en aproximacion lineal: ",estadistico.get_aprox_lin())
    print("Respuesta en aproximacion cuadratica: ",estadistico.get_aprox_cuad())
    estadistico.get_grafica_lineal()
    estadistico.get_grafica_cuadratica()
    time.sleep(3)

def metodo8():
    print("                  Raiz Cuadratica.")
    print("Ingrese los valores a,b,c...")
    __a = input("Ingrese a: ")
    __b = input("Ingrese b: ")
    __c = input("Ingrese c: ")
    cuadratica = RaizCuadratica()
    cuadratica.set_variables(__a, __b, __c)
    cuadratica.get_calcular()
    cuadratica.get_grafica()
    time.sleep(3)
    
def metodo9():
    print("")
    print("                 MÉTODO DE LA SECANTE")
    print("")
    M_secante = Secante()
    M_secante.get_secante()
    time.sleep(3)


def menu():
    operacion = 0
    while operacion != 10:
        print("||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||                   Menu                     ||")
        print("||           1. Método de Ruffini.            ||")
        print("||           2. Falsa posición.               ||")
        print("||           3. Newton raphson.               ||")
        print("||           4. Area de integrales.           ||")
        print("||           5. Eliminacion de gauss.         ||")
        print("||           6. Método de bisección.          ||")
        print("||           7. Método estadistico.           ||")
        print("||           8. Raiz cuadratica.              ||")
        print("||           9. Método de la secante.         ||")
        print("||           10. Salir del programa.          ||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||")
        operacion = int(input("Digite la Opcion: "))
        if operacion == 1:
            metodo1()
        elif operacion == 2:
            metodo2()
        elif operacion == 3:
            metodo3()
        elif operacion == 4:
            metodo4()
        elif operacion == 5:
            metodo5()
        elif operacion == 6:
            metodo6()
        elif operacion == 7:
            metodo7()
        elif operacion == 8:
            metodo8()
        elif operacion == 9:
            metodo9()
        elif operacion == 10:
            exit
        system('cls')
menu()