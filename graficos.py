# -*- coding: utf-8 -*-


import sys, pygame
import nucleo
from pygame.locals import *

WIDTH = 700
HEIGHT = 700














def load_image(filename):
	"""Carga la imagen de la ruta que se pasa como argumento"""

    try:
    	image = pygame.image.load(filename)
    
    except pygame.error.message:
        raise SystemExit.message

    image = image.convert()
    
    return image


def cargarImagenes():
	"""Carga una serie de imagenes necesarias para representar el 'juego'"""
	
	azul=load_image("images/azul.png")
	cabazul=load_image("images/cabazul.png")
	azulchoque=load_image("images/azulchoque.png")
	azulvacio=load_image("images/azulvacio.png")

	rojo=load_image("images/rojo.png")
	cabrojo=load_image("images/cabrojo.png")
	rojochoque=load_image("images/rojochoque.png")
	rojovacio=load_image("images/rojovacio.png")
	choquetotal=load_image("images/choquetotal.png")
	error=load_image("images/verde.png")


	return azul,cabazul,azulchoque,azulvacio,rojo,cabrojo,rojochoque,rojovacio,choquetotal,error


def texto(texto):
	"""Presenta texto en la pantalla"""
	color=(0, 0, 0)
	fuente = pygame.font.Font("images/DroidSans.ttf", 25)
	salida = pygame.font.Font.render(fuente, texto, 1, color)	
	return salida


def dibujaMatriz(matriz,screen,images):
	"""Esta funcion se encarga de dibujar en pantalla la matriz pasada como argumento.
	En 'images' se deberá pasar una tupla de imagenes para tal fin."""
	 
	 for y in range(102):
	 	for x in range(102):
	 		ordenadas=44+6*y
	 		abscisas=44+6*x
	 		if matriz[y][x]==3:
	 			screen.blit(images[1],(abscisas,ordenadas))
	 		elif matriz[y][x]==4:
	 			screen.blit(images[0],(abscisas,ordenadas))
	 		elif matriz[y][x]==13:
	 			screen.blit(images[5],(abscisas,ordenadas))
	 		elif matriz[y][x]==15:
	 			screen.blit(images[4],(abscisas,ordenadas))
	 		elif matriz[y][x]==18:
	 			screen.blit(images[2],(abscisas,ordenadas))
	 		elif matriz[y][x]==34:
	 			screen.blit(images[3],(abscisas,ordenadas))
	 		elif matriz[y][x]==17:
	 			screen.blit(images[6],(abscisas,ordenadas))
	 		elif matriz[y][x]==44:
	 			screen.blit(images[7],(abscisas,ordenadas))
	 		elif matriz[y][x]==16:
	 			screen.blit(images[8],(abscisas,ordenadas))
	 		elif matriz[y][x]==7:
	 			screen.blit(images[2],(abscisas,ordenadas))
	 		elif matriz[y][x]==28:
	 			screen.blit(images[6],(abscisas,ordenadas))
	 		elif not(matriz[y][x]==0):
	 			screen.blit(images[9],(abscisas,ordenadas))






def mostrarResultado(resultado,screen):
	"""Muestra un texto con el resultado."""

	coordenadas=(250,300)
	textoAux=texto("Error")

	if resultado[0]==1:
		textoAux=texto("Jugador 1 gana")
		
	elif resultado[0]==2:
		textoAux=texto("Jugador 2 gana")

	elif resultado[0]==3:

		if resultado[1]==10:
			textoAux=texto("¡Ostia terrible!")
		
		else:
			textoAux=texto("Empate")


	screen.blit(textoAux,coordenadas)




def visualizarMatriz(matriz):
	"""Este metodo ofrece una version grafica de la matriz pasada como argumento"""

	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Instantanea")
	clock = pygame.time.Clock()
	background= load_image('images/fondo.png')
	images=cargarImagenes()

	

	time=clock.tick(60)

	screen.blit(background,(50,50))
	dibujaMatriz(matriz,screen,images)
	pygame.display.flip()


	while True:

		keys=pygame.key.get_pressed()

		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)






def main(uno,dos):
	"""Como su propio nombre indica, la funcion principal. inicia un juego entre los jugadores
	pasados como argumento.
	NOTA: Para reiniciar el juego, hay que pulsar 'Backspace'"""
	
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pruebas Tron")
	clock = pygame.time.Clock()
	background= load_image('images/fondo.png')
	images=cargarImagenes()

	
	matriz=nucleo.creaMatriz(102)
	
	
	matriz[50][25]=3
	matriz[50][75]=13
	

	while True:
		time=clock.tick(60)		
		keys=pygame.key.get_pressed()

		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
		

		resultado=nucleo.resultado(matriz)
		
		if keys[K_BACKSPACE]:
			matriz=nucleo.creaMatriz(102)
			matriz[50][25]=3
			matriz[50][75]=13

		

		if resultado[0]==0:

			direct=uno.actualizar(matriz)
			matriz=nucleo.actualizaMatriz(matriz,1,direct)

			direct=dos.actualizar(matriz)
			matriz=nucleo.actualizaMatriz(matriz,2,direct)			

		
		screen.blit(background,(50,50))
		dibujaMatriz(matriz,screen,images)

		if not resultado[0]==0:
			
			mostrarResultado(resultado,screen)



		pygame.display.flip()


		







		
		

