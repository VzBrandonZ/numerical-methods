import numpy
import matplotlib.pyplot as plt
import numpy as np



class Secante():

    def get_secante(self):

        function = input("Ingrese la funcion: ")
        f = lambda x: eval(function)
        xi = float(input('Introduce el valor de inicio xi: '))
        x0 = float(input('Introduce el valor de inicio x0: '))
        epsilo=float(input('Introduce el epsilo '))
        error=1e-1
        i=0
        print ('                                MÉTODO DE LA SECANTE                                   ')
        print('{:^3}\t\t{:^16}\t\t{:^16}'.format('i','raiz','Error'))
        print('____________________________________________________________________________')
        while abs(error) > epsilo :
            x2 = xi - (f(xi)*(xi-x0))/(f(xi)-f(x0))   
            error= abs(x2-xi)
            i=i+1
            x0 = xi
            xi = x2
            print('{:^3}\t\t{:^16}\t\t{:^16}'.format(i,x2,error))
        
        print('')    
        print('La raiz es: ',x2, 'y fue encontrada con: ',i,'interaciones')
        x= np.linspace (0, 4, 200)
        plt.plot(x, f(x))
        plt.title('Gráfico del ejercicio')
        y=0
        linea = [y]*5
        plt.plot(linea)
        plt.plot(xi, f(xi), 'or')
        plt.grid()
        plt.show()