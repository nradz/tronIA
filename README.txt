tronIA 1.0

El objetivo de esta aplicación es ofrecer una serie de funciones y métodos con los que sea posible
crear un sistema de inteligencia artificial para un juego del estilo de las motos de "Tron", la 
famosa película de 1982, con fines didácticos.
Concretamente, se tendrá que programar un jugador que deberá elegir la próxima dirección hacia la 
que se moverá en un tablero.


->Aprender

El interés principal que tengo con esta aplicación es que, aquellos que queramos participar, podamos
practicar y mejorar nuestros conocimientos de forma colaborativa.
Para ello, quien desee crear un "bot" para tronIA sería conveniente que hiciera un "fork" del 
repositoria e incluyera código de su bot, de esa forma se podrá visualizar desde Github todos aquellos
que hayan participado.


->Requisitos

El código ha sido programado en python 3.x usando la librería Pygame, que deberá ser instalada para
poder ejecutar la aplicación.
AVISO: Pygame para python 3.x es diferente que el de versiones anteriores, por lo que hay
que tener cuidado cual se va a instalar y escoger el adecuado.


->Los diferentes archivos

graficos.py : Aquí se encuentran todo lo necesario para poder poder ver por pantalla el 'juego'.
nucleo.py : Métodos y funciones que permiten resolver enfrentamientos entre jugadores.
motos.py : En este código se encuentra la clase de la que deben extender los bots que se creen.
jugador.py : Código que incluye una redefinición de Moto que permite a un jugador 'real' competir
			contra un bot o contra otro jugador. Cabe destacar que solo funciona en la versión gráfica.
LICENSE.txt : La licencia de tronIA.
images: Carpeta que incluye todas las imágenes necesarias para la parte gráfica.


->Documentación

La documentación está disponible en los propios documentos de código. En un futuro, se pretende crear
un adicional externo para tal fin.


->La matriz

Tras observar la documentación, se habrá visto que el "juego" gira en torno a una matriz y a los valores
que se hayan en esta.
A continuación, se explica que significa cada valor:

0: Una posición vacía.
3: La 'moto', la 'cabeza' del jugador 1.
4: La 'cola', la estela del jugador 1.
13: La 'moto', la 'cabeza' del jugador 2.
15: La 'cola', la estela del jugador 2. 
31: El borde de la matriz.
18: Jugador 1 se ha estrellado con la estela del jugador 2.
34: Jugador 1 se ha estrellado con el borde del "tablero".
7: Jugador 1 se choca con su propia estela.
17: Jugador 2 se choca con la estela del jugador 1.
44: Jugador 2 se ha estrellado con el borde del "tablero".
38: Jugador 2 se choca con su propia estela.
16: Ambas "motos" se chocan mútuamente.

