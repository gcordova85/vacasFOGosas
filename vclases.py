import threading
from threading import Thread, Lock

class Vaca:
	def __init__ (self, nombre, estaViva, estaLista, celo, peso, nocome, cria):
		self.nombre=nombre
		self.estaViva=estaViva
		self.estaLista=estaLista
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
	def getEstaLista(self):
		return self.estaLista
	def setEstaLista(self,estado):
		self.estaLista = estado
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
		self.cria=self.cria
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


class Pasto():
	#Constructor
	def __init__ (self, disponibilidad=100):
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
			print "\n"+"El pasto esta siendo comido"+"\n"+"Queda", self.disponibilidad, "de pasto"+"\n"
			return True
		else:
			print "entra"
			optima = Optima()
			p1=threading.Thread(target=optima.sembrar, args=(self,))
			p1.start()
			return False
			# Crear una linea concurrente nueva que pida un esfuerzo.
			# Una vez que tenga el esfuerzo en mano pregunta si hay pasto suficiente y si lo hay no siembra.


class Optima():

	def sembrar(self, campo):
		with disponibilidad:
			# Como es probable que mas de una vaca llame al metodo solo se activa si el pasto es menor al 10%
			if campo.getDisponibilidad() < campo.getDispInicial()*0.1:
				print "\n"+"Resembrando pasto"+"\n"
				campo.setDisponibilidad(campo.getDispInicial()) 
	

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

esfuerzo = Esfuerzo(1)
cantidad = esfuerzo.getEsfuerzo()
disponibilidad = threading.BoundedSemaphore(value=cantidad)