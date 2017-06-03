class Vaca:
	def __init__ (self,estaViva=True,estaLista=False,celo=False,peso=150,nocome=0):
		self.estaViva=estaViva
		self.estaLista=estaLista
		self.celo=celo
		self.peso=peso
		self.nocome=nocome

	#Getters & Setters
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
		return self.celo
	def setPeso(self,peso):
		self.peso=peso
		return self.peso
	def getNoCome(self):
		return self.nocome
	def setNoCome(self, dias):
		self.nocome=self.nocome+dias
		return self.nocome

	#Metodos
	def morir(self):
		print "\n"+"=====Martillazo a la vaca====="+"\n"+"Vaca desafortunada: adios muuuundo cruel x_x"+"\n"
		self.estaViva=False
	def engordar(self):
		self.peso=self.peso+1.2
	def incremento(self):
		aux=self.peso*0.1
		return aux



class Pasto():
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
			print "\n"+"El pasto esta siendo comido"+"\n"+"Queda", self.disponibilidad, "de pasto"+"\n"
		else:
			self.disponibilidad=0
	
	def sembrar(self):
		#SOLO si hay esfuerzo disponible
		print "\n"+"Resembrando pasto"+"\n"
		self.disponibilidad = self.dispInicial
	
	

class Esfuerzo():
	#Constructor
	def __init__ (self, personas=0):
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
