from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class RaizCuadratica():
	#Ingreso de los valores de A B y C en el setter.
	def set_variables(self, a, b, c):
		
		self.__a=float(a)
		self.__b=float(b)
		self.__c=float(c)
				

	#Getter para poder calcular el valor de la determinante y de las raices(x1,x2) 			
	def get_calcular(self):
		self.__determinante=(self.__b**2)-(4*self.__a*self.__c)
		if self.__determinante<=0:
			x1=round((-self.__b/(2*self.__a)),2)
			return x1
		else:
			self.__x1=round(((-self.__b+sqrt(self.__determinante))/(2*self.__a)),2)
			self.__x2=round(((-self.__b-sqrt(self.__determinante))/(2*self.__a)),2)
			return print("Raiz x1: {} Raiz x2: {}".format(self.__x1,self.__x2))
	#Grafica donde se visualiza los dos puntos de raiz (x1, x2)
	def get_grafica(self):	
		f=lambda x:(self.__a*x**2+self.__b*x+self.__c)
		m=np.linspace(-10,10)
		plt.plot(m,f(m))
		plt.plot(m,f(m)*0)
		plt.plot(self.__x1,f(self.__x1), 'or')
		plt.plot(self.__x2,f(self.__x2), 'or')
		plt.grid()
		plt.show()
		
			