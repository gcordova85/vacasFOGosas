from threading import Thread, Lock
import time
from random import randint



sillas = 0
invitados = []
procesos = []
lock = Lock()

# Este es el comportamiento de los que ya tienen su comida, solo pueden ir sentandose una vez que se desocupa una silla (cada 2 a 5 seg.). El programa empieza con una cantidad 
# dada de clientes esperando para sentarse.
def comer(nombre):
	global lock
	with lock:
		global sillas
		print "comiendo"
		tiempoDeEspera = randint(2,5)
		time.sleep(tiempoDeEspera)
		# Van en aumento pero deberian ir restandose, es a modo de ejemplo.
		sillas +=1

# Este es el comportamiento de los que vienen entrando, no necesitan esperar nada para hacerlo. Entran cada cierto tiempo.
def entrar():
	tiempoDeEspera = randint(1,20)
	time.sleep(tiempoDeEspera)
	print "nueovo cliente entra"

# Aca se agregan igual cantidad de personas esperando sentarse como personas que van a entrar al local. 
def constructor():
	personas=input("cantidad: ")
	
	for x in range(personas):
		x = Thread(target=comer, args=(x,))
		procesos.append(x)

	for x in range(personas):
		cliente= Thread(target=entrar)
		procesos.append(cliente)

	for z in procesos:
		z.start()

constructor()


