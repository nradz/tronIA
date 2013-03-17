# -*- coding: utf-8 -*-




def creaMatriz(dim):
	"""Crea una matriz de orden dimxdim. Asigna a los 'bordes' el valor 31 y al resto 0"""


	#El primer valor de la matriz sera "y". El segundo "x".
	matriz = [[0] * dim for i in range(dim)]

	matriz[0]=[31]*dim
	matriz[-1]=[31]*dim

	for e in matriz:
		e[0]=31
		e[-1]=31

	return matriz





def buscarValor(matriz,valor):
	"""Busca en la matriz pasada como argumento el valor dado. Solo devuelve la posicion del
	primer valor coincidente. En el caso de no encontrar ninguno, devuelve (-1,-1) """

	res=(-1,-1)

	for y in range(len(matriz)):
		
		aux=matriz[y]
		
		for x in range(len(aux)):

			if matriz[y][x]==valor:
				res=(x,y)

	return res





def existeValor(matriz,valor):
	"""Devuelve True si encuentra en la matriz el mismo valor que
	el pasado como argumento. En caso contrario, devuelve False"""

	res=False

	for y in range(len(matriz)):
		
		aux=matriz[y]
		
		for x in range(len(aux)):

			if matriz[y][x]==valor:
				res=True

	return res





def actualizaMatriz(matriz,jugador,direccion):
	
	"""Dado una matriz, actualiza la posicion del jugador indicado en dicha matriz teniendo en cuenta
	la direccion pasada.
	NOTA: Si en direccion no se pasa un valor valido, se toma por defecto la 'derecha0' """

	matrizAux=matriz

	#Es el valor que tendra la "cabeza" del jugador
	valorJug=0
	valorAdd=0

	if jugador==1:
		valorJug=3
		valorAdd=1
	else:
		valorJug=13
		valorAdd=2

	pos=buscarValor(matriz,valorJug)

	matrizAux[pos[1]][pos[0]] += valorAdd

	if direccion=="up":
		matrizAux[(pos[1]-1)][pos[0]] += valorJug

	elif direccion=="down":
		matrizAux[(pos[1]+1)][pos[0]] += valorJug

	elif direccion=="left":
		matrizAux[pos[1]][(pos[0]-1)] += valorJug

	else:
		matrizAux[pos[1]][(pos[0]+1)] += valorJug

	return matrizAux





def resultado(matriz):
	"""Devuelve una tupla. El primer valor indica el resultado de la matriz.
	( 0 si el "juego" continua, 1 si gana el jugador uno, 2 si gana el jugador 2 y 3 si es empate).
	El segundo valor indica los detalles del resultado."""


	res=0
	detalles=0

	#Se miran los casos del jugador 1.
	#El jugador 1 se choca contra la cola del jugador 2.
	if existeValor(matriz,18):
		res += 2
		detalles = 1
	#El jugador 1 se choca contra la pared.
	elif existeValor(matriz,34):
		res += 2
		detalles = 2
	#El jugador 1 se choca consigo mismo.
	elif existeValor(matriz,7):
		res += 2
		detalles = 3


	#Se miran los casos del jugador 2.
	if existeValor(matriz,17):
		res += 1
		if detalles==1:
			#Los dos se han chocado con la cola del otro a la vez.
			detalles = 7
		else:
			#El jugador 2 se choca contra la cola del jugador 1.	
			detalles = 4
	
	elif existeValor(matriz,44):
		res += 1
		if detalles==2:
			#Ambos jugadores se chocan contra la pared a la vez.
			detalles = 8
		else:
			#El jugador 2 se choca contra la pared.
			detalles = 5
	
	elif existeValor(matriz,28):
		res += 1
		if detalles==3:
			#Ambos jugadores se chocan consigo mismo.
			detalles = 9
		else:
			#El jugador 2 se choca consigo mismo.
			detalles = 6

	#Caso especial de choque de "cabezas"
	if existeValor(matriz,16):
		res = 3
		detalles = 10

	return res,detalles



def combate(jugador1,jugador2):
	"""En este metodo se resolvera una "partida" entre jugador1 y jugador 2.
	Si gana el primero, se devolverá 1, si gana el segundo, 2 y si es empate, 3."""

	matriz=creaMatriz(102)

	#Se colocan a los jugadores en el tablero.
	matriz[50][25]=3
	matriz[50][75]=13

	res=(0,0)

	#El bucleo se repite hasta que el resultado sea distinto de cero.
	while res[0]==0:

		#Se obtienen las direcciones que tomara cada jugador.
		direct1=jugador1.actualizar(matriz)
		direct2=jugador2.actualizar(matriz)

		#Se actualiza la matriz moviendo a cada jugador.
		matriz=actualizaMatriz(matriz,1,direct1)
		matriz=actualizaMatriz(matriz,2,direct2)

		res=resultado(matriz)


	return res





def combatePasoAPaso(jugador1,jugador2):
	"""Este metodo, en vez de devolver el resultado, devuelve una lista con cada una de las iteraciones de la matriz"""

	#Esta sera la lista donde se guardaran las iteraciones de la matriz.
	matrizRes=[]

	matriz=creaMatriz(102)

	matriz[50][25]=3
	matriz[50][75]=13

	#Se almacena la primera iteracion.
	matrizRes.append(matriz)


	res=(0,0)

	#El bucleo se repite hasta que el resultado sea distinto de cero.
	while res[0]==0:
		direct1=jugador1.actualizar(matriz)
		direct2=jugador2.actualizar(matriz)

		matriz=actualizaMatriz(matriz,1,direct1)
		matriz=actualizaMatriz(matriz,2,direct2)

		#Se almacena cada una de las iteraciones.
		matrizRes.append(matriz)

		res=resultado(matriz)


	return matrizRes





def torneo(jugador1,oponentes,num):
	"""oponentes es una lista de jugadores. Jugador 1 se enfrentará con cada uno tantos combates como diga num.
	El resultado será una lista donde cada posicion corresponde a un oponente. Dentro de dicha posicion, habra
	otra lista con los resultados de cada combate."""


	res=[]

	for i in range(len(oponentes)):
		res.append([])
		
		for e in range(num):
			aux=combatePasoAPaso(jugador1,oponentes[i])
			res[i].append(aux)



	return res




	



def mostrarMatriz(matriz):
	"""Muestra la matriz de forma simplificada, para 'testeos' de la aplicacion"""

	print("------------")
	for i in matriz:
		print (i)







