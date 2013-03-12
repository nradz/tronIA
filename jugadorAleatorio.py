import motos

import random



class JugadorAleatorio(motos.Moto):

	def __init__(self):

		motos.Moto.__init__(self)
		self.ops=["right","left","up","down"]
		self.direct=random.choice(self.ops)


	def actualizar(self,matriz):

		aux=random.choice(self.ops)

		self.direct=aux

		return self.direct