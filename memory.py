from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2  # Esto se puede cambiar por imágenes si decides usar imágenes en vez de dígitos
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable global para contar taps

# Lista de imágenes para innovar (si decides usar imágenes en lugar de números)
images = ['apple.gif', 'banana.gif', 'cherry.gif', 'dog.gif', 'elephant.gif']

def square(x, y):
    "Dibuja un cuadro blanco con borde negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convierte las coordenadas (x, y) a un índice de los cuadros."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte el contador de cuadros a coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    global tap_count
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    # Incrementar el contador de taps
    tap_count += 1

def all_revealed():
    "Verifica si todos los cuadros están destapados."
    return all(not state for state in hide)  # Todos los cuadros están destapados

def win_message():
    "Muestra un mensaje de victoria cuando todos los cuadros estén destapados."
    up()
    goto(0, 0)
    color('red')
    write("¡Felicidades! ¡Has ganado!", align="center", font=('Arial', 24, 'normal'))

def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # Centrar el dígito o imagen en el cuadro
        image = tiles[mark]
        addshape(image)  # Añadir la imagen como forma en turtle
        shape(image)
        stamp()

    # Mostrar el número de taps
    up()
    goto(-180, 180)  # Ubicación en pantalla para el contador de taps
    color('black')
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))

    # Verificar si todos los cuadros están destapados
    if all_revealed():
        win_message()

    update()
    ontimer(draw, 100)

# Mezcla las imágenes para los tiles
def shuffle_images():
    shuffled_images = images * 2  # Duplica las imágenes para hacer pares
    shuffle(shuffled_images)
    return shuffled_images

tiles = shuffle_images()  # Reemplaza los números con imágenes

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
