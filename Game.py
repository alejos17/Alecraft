#Creado por: Alejandro Tamayo
#Fecha: 11-Nov-2021
#Descripcion: Juego estilo minecraft usando ursina engine

from ursina import *
# Importar una instancia de Jugador
from ursina.prefabs.first_person_controller import FirstPersonController

#Nueva App con la libreria
app = Ursina()

#Instancia en clase Voxel de Button Ursina que trae metodos listos
class Voxel(Button):
    
    #Iniciar el plano con cubos y colores con textura grass
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'grass',
            color = color.rgb(255, 255, 255),
            highlight_color = color.lime,
        )

    #Funcion para dar clic izquierdo poner bloque
    #Funcion con clic derecho para quitar bloque
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)

#Definir tamaño del chuck de minecraft
chunkSize = 16

#Rellenar el terreno con bloques de grass
for z in range(chunkSize):
    for x in range(chunkSize):
        voxel = Voxel(position=(x, 0, z))

#Instanciar un Jugador en la escena
player = FirstPersonController(position=(0, 0, 0))

#Correr la app
app.run()
