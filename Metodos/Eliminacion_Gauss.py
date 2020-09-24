import numpy

class Eliminacion_Gauss():

	def gauss(self):
		print ('')
		print ('			ELIMINACIÓN GAUSS')
		print ('')
		m=int(input('Valor de m:'))

		n=int(input('Valor de n:'))

		matrix = numpy.zeros((m,n))

		vector= numpy.zeros((n))
		x=numpy.zeros((m))

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