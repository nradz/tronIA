import pygame
import motos
from pygame.locals import *


class Jugador(motos.Moto):
    """Clase para crear jugadores 'reales'.
    Solo se puede pasar una instancia de este
    objeto a graficos.main(), ya que en cualquier otro caso
    dara error ya que no esta iniciado 'pygame'"""

    def __init__(self, jugador):

        motos.Moto.__init__(self, jugador)
        self.direct = ""

        if jugador == 1:
            self.direct = "right"
        else:
            self.direct = "left"

    def actualizar(self, matriz):

        matrizAux = matriz

        keys = pygame.key.get_pressed()

        if self.jugador == 1:
            if keys[K_w]:
                self.direct = "up"
            elif keys[K_s]:
                self.direct = "down"
            elif keys[K_a]:
                self.direct = "left"
            elif keys[K_d]:
                self.direct = "right"

        else:
            if keys[K_UP]:
                self.direct = "up"
            elif keys[K_DOWN]:
                self.direct = "down"
            elif keys[K_LEFT]:
                self.direct = "left"
            elif keys[K_RIGHT]:
                self.direct = "right"

        return self.direct
