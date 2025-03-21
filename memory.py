# Variable global para contar taps
tap_count = 0

def tap(x, y):
    global tap_count  # Accede a la variable global
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    # Incrementa el contador de taps
    tap_count += 1

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
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps
    up()
    goto(-180, 180)  # Ubicación en pantalla para el contador de taps
    color('black')
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)
