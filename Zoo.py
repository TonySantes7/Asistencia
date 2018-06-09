# Santes Mejia Antonio
print "...Tecnicas de programacion.."

class Especies:
	nombre=[]	
	edad=[]
	color=[]

	def __init__(self,nombre,edad,color):
		self.nombre=nombre
		self.edad=edad
		self.color=color		
		

class Ganzo(Especies):
	pico=None
	pluma=None
	canto=None
	def __init__(self,nombre,edad,color,pico,pluma,canto):
		Especies.__init__(self,nombre,edad,color)
		self.pico=pico
		self.pluma=pluma
		self.canto=canto
	pass

class tigre(Especies):
	tamano=None
	piel="suave"
	comida=None
	def __init__(self,nombre,edad,color,tamano,piel,comida="Carne"):
		Especies.__init__(self,nombre,edad,color)
		self.tamano=tamano
		self.comida="carne"
	pass

class Hipopotamo(Especies):
	tamano=None
	piel=None
	sexo=None
	def __init__(self,nombre,edad,color,tamano,piel,sexo):
		Especies.__init__(self,nombre,edad,color)
		self.tamano=tamano
		self.piel=piel
		self.sexo=sexo
	pass

class Elefante(Especies):
	comida=None
	piel=[]
	sexo=[]
	def __init__(self,nombre,edad,color,comida,piel,sexo):
		Especies.__init__(self,nombre,edad,color)
		self.comida=comida
		self.piel=piel
		self.sexo=sexo
	pass

class Cebra(Especies):
	sexo=[]
	sonido=[]
	caracter=[]
	def __init__(self,nombre,edad,color,sonido,caracter,sexo):
		Especies.__init__(self,estado,edad,color,nombre)
		self.sonido=sonido
		self.caracter=caracter
		self.sexo=sexo
pass
