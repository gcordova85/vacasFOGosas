import time
import threading
from vclases import *

comida=Pasto()
		
def vacaVive():
	vaca=Vaca()
	pasarDias(vaca, 120, False, False, 0)


# ----- IMPORTANTE-------
# Este codigo va pasando los dias y en base a ellos va activando eventos relacionados a la vida de la vaca.
def pasarDias(vaca, diaActual, celo, cria, sinComer)
	dia = diaActual
	if comida.getDisponibilidad > 0:
		# Aca habria que ver si va a llamar a optima para que vea el pasto o eso pasa en otro lado.
		comida.comer(vaca.incremento())
		vaca.engordar()
		sinComer=0
	else:
		if sinComer == 7:
			# Muere la vaca y se quita su proceso del multithreading.
		else:
			sinComer+=1
			vaca.adelgazar()
			# Avisa a esfuerzo que necesita comida
	# El celo llega cada 21 dias y tarda una solo.
	if celo == 21:
		# Vaca entra en celo y optima se fija si la insemina
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
		# Optima se fija si es momento de sacrificar.
	dia +=1


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
			