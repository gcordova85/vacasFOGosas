import time
import threading
from vclases import *

comida=Comida()


		
def vacaVive(nombre):
	vaca=Vaca(nombre, True, False, 300, 0, False)
	# nombre, estaViva, estaLista, celo, peso, nocome, cria
	pasarDias(vaca, 350, 0, False, 0)
	# vaca, diaActual, celo, cria, sinComer


# ----- IMPORTANTE-------
# Este codigo va pasando los dias y en base a ellos va activando eventos relacionados a la vida de la vaca.
def pasarDias(vaca, diaActual, celo, cria, sinComer):
	if vaca.getEstaViva() == False:
		exit()
	# PONGO EL EXIT PARA SACAR CAPTURA
	if diaActual == 367:
		exit()
	dia = diaActual
	print "-----------------------"
	print vaca.getNombre() + ". Edad: " + str(dia) + " dias." + " Peso: " +str(vaca.getPeso()) + " Kilos." +" Dia de celo: "+str(celo)
	if comida.comer(vaca.incremento()) == True:
		vaca.engordar()
		# -------------------------- IMPORTANTE -----------------------
		# Yo pondria sinComer como atributo de VACA para que optima pueda ver si debe inseminar cuando la vaca esta hambreada.
		sinComer = 0
	else:
		if sinComer == 7:
			print vaca.getNombre()+"vaca murio"
			pass
			exit()
			# Muere la vaca y se quita su proceso del multithreading.
		else:
			print "Sin alimento."
			sinComer+=1
			vaca.adelgazar()
			# El pasto le avisa a Esfuerzo que necesita comida
	# El celo llega cada 21 dias y tarda una solo.
	if celo == 21:
		vaca.setCelo(True)
		vaca.entrarCelo()
		celo +=1
		# Optima se fija si la insemina
		# Si la vaca no fue inseminada hay que cambiar el celo a 0 de vuelta
	if celo> 21:
		vaca.setCelo(False)
		celo = 0
	if vaca.getCria()==True:
		# Dias que tarda en nacer una vaca
		if cria < 283:
			cria +=1
			celo = 0
		else:
			#Nace la cria
			print "Ha nacido la cria"
			vaca.setCria(False)
			celo = -24
	if celo<21 and vaca.getCria() == False:
		celo+=1
	if vaca.getCria() == False and dia > 365:
		vaca.irMatadero()
		# Optima se fija si es momento de sacrificar.
	dia +=1
	fallaProbabilidad = fallo.probabilidad()
	if fallaProbabilidad == "hambreError":
		print "Algo fallo con la comida!"
		sinComer = 6
	elif fallaProbabilidad == "criaError":
		print "Algo fallo con la cria!"
		vaca.setCria(False)
		exit()
	elif fallaProbabilidad == "celoError":
		print "Algo fallo con el celo"
		vaca.setCelo(-10)
		exit()
	time.sleep(0.1)
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
			
