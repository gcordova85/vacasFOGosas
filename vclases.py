import threading
from threading import Thread, Lock
from random import randint

class Vaca:
	def __init__ (self, nombre, estaViva, celo, peso, nocome, cria):
		self.nombre=nombre
		self.estaViva=estaViva
		#~ self.estaLista=estaLista
		self.celo=celo
		self.peso=peso
		self.nocome=nocome
		self.cria=cria

	#Getters & Setters
	def getNombre(self):
		return self.nombre
	def setNombre(self, nombre):
		self.nombre = nombre
		return self.nombre
	def getEstaViva(self):
		return self.estaViva
	def setEstaViva(self,estado):
		self.estaViva = estado
		return self.estaViva
	#~ def getEstaLista(self):
		#~ return self.estaLista
	#~ def setEstaLista(self,estado):
		#~ self.estaLista = estado
		return self.estaLista
	def getCelo(self):
		return self.celo
	def setCelo(self,celo):
		self.celo=celo
		return self.celo
	def getPeso(self):
		return self.peso
	def setPeso(self,peso):
		self.peso=peso
		return self.peso
	def getNoCome(self):
		return self.nocome
	def setNoCome(self, dias):
		self.nocome=self.nocome+dias
		return self.nocome
	def getCria(self):
		return self.cria
	def setCria(self, cria):
		self.cria=cria
		return self.cria

	#Metodos
	def morir(self):
		print "\n"+"=====Martillazo a la vaca====="+"\n"+"Vaca desafortunada: adios muuuundo cruel x_x"+"\n"
		self.estaViva=False
	def engordar(self):
		if self.peso < 450:
			self.peso=self.peso+1.2
	def incremento(self):
		aux=self.peso*0.1
		return aux
	def adelgazar(self):
		self.peso=self.peso-1.2
	def entrarCelo(self):
		p1=threading.Thread(target=optima.inseminar, args=(self,))
		p1.start()
	def irMatadero(self):
		p1=threading.Thread(target=optima.matar, args=(self,))
		p1.start()

class Comida():
	#Constructor
	def __init__ (self, disponibilidad=1000):
		self.dispInicial=disponibilidad
		self.disponibilidad=disponibilidad

	#Getters & Setters
	def getDispInicial(self):
		return self.dispInicial
	def setDispInicial(self, cant):
		self.dispInicial=cant
		return self.dispInicial
	def getDisponibilidad(self):
		return self.disponibilidad
	def setDisponibilidad(self,cant):
		self.disponibilidad=cant
		return self.disponibilidad
	#Metodos
	def comer(self,consumo):
		if consumo < self.disponibilidad:
			self.disponibilidad=self.disponibilidad-consumo
			print "\n"+"Se alimento con el pasto."+"\n"+"Quedan", self.disponibilidad, "kilos disponibles."+"\n"
			return True
		else:
			p1=threading.Thread(target=optima.sembrar, args=(self,))
			p1.start()
			return False
			# Crear una linea concurrente nueva que pida un esfuerzo.
			# Una vez que tenga el esfuerzo en mano pregunta si hay pasto suficiente y si lo hay no siembra.


class Optima():

	def sembrar(self, campo):
		with disponibilidad:
			# Como es probable que mas de una vaca llame al metodo solo se activa si el pasto es menor al 10%
			if campo.getDisponibilidad() < campo.getDispInicial()*0.2:
				print "\n"+"Optima ha decidido sembrar."+"\n"
				campo.setDisponibilidad(campo.getDispInicial()) 
	
	def inseminar(self, vaca):
		with disponibilidad:
			#Aca habria que ver si realmente vale la pena inseminar por medio de calculos de varias variables. (Ej: cant. maxima de ganado soportado)
			if vaca.getPeso() < 200:
				print "Optima ha decidido no inseminar por bajo peso."
			else:
				vaca.setCria(True)
				print "Optima ha decidido inseminar"

	def matar(self, vaca):
		with disponibilidad:
			if vaca.getPeso() < 400:
				print "Vaca demasiado delgada"
				return False
			else:
				print "Vaca llevada al matadero"
				vaca.morir()

class Esfuerzo():
	#Constructor
	def __init__ (self, personas):
		self.personas=personas
	
	#Getters & Setters
	def getEsfuerzo(self):
		return self.personas
	def setEsfuerzo(self, cant):
		self.personas=cant
		return self.personas
	
	#Metodos
	def tomar(self, cant):
		print "Se contratan "+str(cant)+" persona/s"
		self.personas=self.personas+cant

	def rajar(self,cant):
		print "Se despiden "+str(cant)+" persona/s"
		self.personas=self.personas-cant
	def matar(self,vaca):
		pass
	def sembrar(self, comida):
		pass
	def inseminar(self, vaca):
		pass
		
class Falla():
	def probabilidad(self):
		random = randint(0,30)
		if random == 0:
			return "hambreError"
		elif random == 1:
			return "criaError"
		elif random == 2:
			return "celoError"
	




esfuerzo = Esfuerzo(1)
cantidad = esfuerzo.getEsfuerzo()
disponibilidad = threading.BoundedSemaphore(value=cantidad)
optima = Optima()
fallo = Falla()
