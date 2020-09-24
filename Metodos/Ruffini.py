

class Ruffini():
	#Ingreso de la funcion con el metodo Setter
	def set_polinomios(self,coeficientes):
		self.__raices=[]
		self.lista=coeficientes.split(',')
		for i in range(len(self.lista)):
			self.lista[i]=float(self.lista[i])

		
	#Getter para poder retornar el resultado de ruffini
	def get_resultado(self):
		
		n=int(self.lista[len(self.lista)-1])
		multiplos=[]
		# Obtengo los multiplos
		for i in range(n):
			if i!=0:	
				if n%i==0:
					multiplos.append(i)
					multiplos.append(-i)
		# Obtengo las raices
		for i in multiplos:
			s=0
			c=0
			lista2=[]
			for j in range(len(self.lista)):
				c+=1
				if c == 1:
					s=self.lista[j]
					lista2.append(s)
				else:
					s=i*s+self.lista[j]
					lista2.append(s)
				if s == 0 and j ==	len(self.lista)-1:
					self.__raices.append(i)
					self.lista=lista2[:-1]

		return print("Raices: ",self.__raices)	

"""r=Ruffini()
r.set_polinomios("1,-1,-4,4")
r.get_resultado()"""

		
		