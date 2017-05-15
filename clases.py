class Vaca:
	#Constructor, el estado default es "viva" ya que no tiene sentido agregar una vaca muerta al campo
	def __init__ (self,celo,peso,edad,raza,fechaIngreso,fechaEgresoEstimado):
		self.__estado="viva"
		self.__celo=celo
		self.__peso=peso
		self.__edad=edad
		self.__raza=raza
		self.__fechaIngreso=fechaIngreso
		self.__fechaEgresoEstimado=fechaEgresoEstimado

	#Getters & Setters
	def getEstado(self):
		return self.__estado
	def setEstado(self,estado):
		self.__estado=estado
		return self.__estado

	def getCelo(self):
		return self.__celo
	def setCelo(self,celo):
		self.__celo=celo
		return self.__celo

	def getPeso(self):
		return self.__celo
	def setPeso(self,peso):
		self.__peso=peso
		return self.__peso

	def getEdad(self):
		return self.__edad
	def setEdad(self,edad):
		self.__edad=edad
		return self.__edad

	def getRaza(self):
		return self.__raza
	def setRaza(self,raza):
		self.__raza=raza
		return self.__raza

	def getFechaIngreso(self):
		return self.__fechaIngreso
	def setFechaIngreso(self,fecha):
		self.__fechaIngreso=fecha
		return self.__fechaIngreso

	def getFechaEgresoEstimado(self):
		return self.__fechaEgresoEstimado
	def setFechaEgresoEstimado(self,fecha):
		self.__fechaEgresoEstimado=fecha
		return self.__fechaEgresoEstimado

	#Metodos


class Comida:
	#Constructor
	def __init__ (self,tipo,disponibilidad):
		self.__tipo=tipo
		self.__disponibilidad=disponibilidad

	#Getters & Setters
	def getTipo(self):
		return self.__tipo
	def setTipo(self, tipo):
		self.__tipo=tipo
		return self.__tipo
	def getDisponibilidad(self):
		return self.__disponibilidad
	def setDisponibilidad(self,disponibilidad):
		self.__disponibilidad=disponibilidad
		return self.__disponibilidad

	#Metodos
	

class Area:
	#Constructor
	def __init__(self):
		self.__posicion=""
		self.__porcentajeOcupacion=""
		self.__porcentajeOptimo=""

	#Getters & Setters
	def getPosicion(self):
		return self.__posicion
	def setPosicion(self, posicion):
		self.__posicion=posicion
		return self.__posicion
	def getPorcentajeOcupacion(self):
		return self.__porcentajeOcupacion
	def setPorcentajeOcupacion(self, porcentaje):
		self.__porcentajeOcupacion=porcentaje
		return self.__porcentajeOcupacion
	def getPorcentajeOptimo(self):
		return self.__porcentajeOptimo
	def setPorcentajeOptimo(self, porcentaje):
		self.__porcentajeOptimo=porcentaje
		return self.__porcentajeOptimo

	#Metodos

class Campo:
	#Constructor:
	def __init__(self,areasVertical,areasHorizontal):
		self.__areasVertical=areasVertical
		self.__areasHorizontal=areasVertical
		self.__campo=[]
	
	#Getters & Setters
	def getAreasVertical(self):
		return self.__areasVertical
	def setAreasVertical(self, areas):
		self.__areasVertical=areas
		return self.__areasVertical
	def getAreasHorizontal(self):
		return self.__areasHorizontal
	def setAreasHorizontal(self, areas):
		self.__areasHorizontal=areas
		return self.__areasHorizontal
	def getCampo(self):
		return self.__campo
	def setAreasVertical(self, campo):
		self.__campo=campo
		return self.__campo
	
	#Metodos
	def buildCampo(self):
		for i in range(self.getAreasVertical()):
			self.getCampo().append([])
    		for j in range(self.getAreasHorizontal()):
        		self.getCampo()[i].append(Area())
		return self.getCampo()

