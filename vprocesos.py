import time
import threading
from vclases import *

comida=Pasto()

def vacaVive():
	cow=Vaca()
	noFood=0
	global pasto
	if noFood == 7:
		cow.morir()
	while True:
		time.sleep(1)
		if comida.getDisponibilidad > 0:
			print "DENTRO DEL IF"
			comida.comer(cow.getPeso()+cow.incremento())
			cow.engordar()
		else:
			print "DENTRO DEL ELSE"
			noFood+=1
			False
			
		
