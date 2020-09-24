import numpy
import matplotlib.pyplot as plt
import numpy as np

class Metodo_biseccion():
    def Biseccion(self):
        """def poli(x):
            y = 0.95*x**3 -5.9*x**2 +10.9*x -6
            return (y)"""
        function = input("Ingrese la funcion: ")
        poli = lambda x: eval(function)
        xi=float(input('Introduce el valor de xi : '))
        xs=float(input('Introduce el valor de xs : '))
        error=float(input('Introduce el epsilo : '))
        print("          MÉTODO DE BISECCIÓN       ")
        xa=(xi+xs)/2
        while abs(poli(xa)) > error:
        
            xa = (xi+xs)/2
            if poli(xi)*poli(xa) < 0:
                xs=xa
                signo="negativo"
                limite="superior"        
            else:
                xi=xa
                signo="positivo"
                limite="inferior" 
        print("La raíz es: ",xa)
        x= np.linspace (0, 4, 50)
        plt.plot(x, poli(x))
        plt.title('Gráfico del ejercicio')
        y=0
        linea = [y]*5
        plt.plot(linea) 
        plt.plot(xi, poli(xi), 'or')
        plt.grid()
        plt.show()

        
        