import time
import threading
from vclases import *

comida=Pasto()
		
def vacaVive(nombre):
	vaca=Vaca(nombre, True, False, False, 150, 0, False)
	pasarDias(vaca, 120, False, False, 0)


# ----- IMPORTANTE-------
# Este codigo va pasando los dias y en base a ellos va activando eventos relacionados a la vida de la vaca.
def pasarDias(vaca, diaActual, celo, cria, sinComer):
	dia = diaActual
	comida.comer(vaca.incremento())
	if comida.comer(vaca.incremento()) == True:
		print comida.getDisponibilidad()
		print vaca.getNombre()
		vaca.engordar()
		sinComer=0
	else:
		if sinComer == 7:
			print vaca.getNombre()+"vaca murio"
			pass
			exit()
			# Muere la vaca y se quita su proceso del multithreading.
		else:
			print vaca.getNombre()+"se muere"
			sinComer+=1
			vaca.adelgazar()
			# El pasto le avisa a Esfuerzo que necesita comida
	# El celo llega cada 21 dias y tarda una solo.
		
	if celo == 21:
		vaca.setCelo(True)
		# Optima se fija si la insemina
		# Si la vaca no fue inseminada hay que cambiar el celo a 0 de vuelta
	if vaca.getCria==True:
		# Dias que tarda en nacer una vaca
		if cria < 283:
			cria +=1
			celo = 0
		else:
			# Vaca termina pariendo y pasan 45 dias antes de entrar en celo
			celo = -24
	if celo<21 and vaca.getCria == False:
		celo+=1
	if vaca.getCria == False and dia > 365:
		pass
		# Optima se fija si es momento de sacrificar.
	dia +=1
	time.sleep(10)
	pasarDias(vaca, dia, celo, cria, sinComer)


# def vacaVive():
# 	cow=Vaca()
# 	noFood=0
# 	global pasto
# 	if noFood == 7:
# 		cow.morir()
# 	while True:
# 		time.sleep(1)
# 		if comida.getDisponibilidad > 0:
# 			print "DENTRO DEL IF"
# 			comida.comer(cow.getPeso()+cow.incremento())
# 			cow.engordar()
# 		else:
# 			print "DENTRO DEL ELSE"
# 			noFood+=1
# 			False
			