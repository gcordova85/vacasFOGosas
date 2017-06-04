import threading
from threading import Thread, Lock
import time
from random import randint




invitados = []
procesos = []
sillas = threading.BoundedSemaphore(value=3)



def comer(nombre):
	with sillas:
		print "comiendo"
		tiempoDeEspera = randint(2,5)
		time.sleep(tiempoDeEspera)

 
def constructor():
	personas=input("cantidad: ")
	
	for x in range(personas):
		x = Thread(target=comer, args=(x,))
		procesos.append(x)

	for z in procesos:
		z.start()

constructor()


