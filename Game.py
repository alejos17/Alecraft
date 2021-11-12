#Creado por: Alejandro Tamayo
#Fecha: 11-Nov-2021
#Descripcion: Juego estilo minecraft usando ursina engine

from ursina import *
# Importar una instancia de Jugador en primera persona
from ursina.prefabs.first_person_controller import FirstPersonController

#Nueva App con la libreria
app = Ursina()

#Se carga las texturas para los bloques
earth_texture = load_texture('texture/platformPack_tile004.png')
water_texture = load_texture('texture/platformPack_tile017.png')
rock_texture = load_texture('texture/platformPack_tile018.png')
wood_texture = load_texture('texture/platformPack_tile034.png')
wall_texture = load_texture('texture/platformPack_tile040.png')
grass_texture = load_texture('texture/platformPack_tile019.png')
stone_texture = load_texture('texture/platformPack_tile016.png')
sky_texture = load_texture('texture/platformPack_tile007.png')
arm_texture = load_texture('texture/platformPack_tile057.png')
on_sound = Audio('audio/000849931_prev.mp3',loop = False, autoplay = False)
destroy_sound = Audio('audio/005903599_prev.mp3',loop = False, autoplay = False)
block_pick = 1  #Bloque por defecto para seleccion

#Opciones para quitar el boton de cierre y los FPS
window.fps_counter.enabled = False
window.exit_button.visible = False

#Funcion de actualizacion constante en el juego
def update():
    global block_pick

    #Condicion para crear la animación de mover la mano al hacer clic sobre un bloque
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7

#Instancia en clase Voxel de Button Ursina que trae metodos listos
class Voxel(Button):
    
    #Iniciar el plano con cubos y colores con textura grass
    def __init__(self, position=(0,0,0), texture=grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
        )

    #Funcion para dar clic izquierdo poner bloque
    #Funcion con clic derecho para quitar bloque
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                on_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = earth_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = water_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = rock_texture)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = wall_texture)
                if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)

            if key == 'right mouse down':
                destroy_sound.play()
                destroy(self)

#Clase para definir el cielo con una esfera al rededor de la escena
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True,
        )

#Clase para la mano del jugador
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            texture = arm_texture,
            scale = .3,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)


#Definir tamaño del chuck de minecraft
chunkSize = 16

#Rellenar el terreno con bloques de grass
for z in range(chunkSize):
    for x in range(chunkSize):
        voxel = Voxel(position=(x, 0, z))

#Instanciar un Jugador en la escena
player = FirstPersonController()
sky = Sky()
hand = Hand()

#Correr la app
app.run()
