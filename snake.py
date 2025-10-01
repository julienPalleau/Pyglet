import pyglet
from pyglet.window import key
import random

# --- Config ---
TAILLE_CASE = 20
NB_CASES_X = 30
NB_CASES_Y = 20
LARGEUR = TAILLE_CASE * NB_CASES_X
HAUTEUR = TAILLE_CASE * NB_CASES_Y
VITESSE = 0.15  # en secondes

# --- Fenêtre ---
window = pyglet.window.Window(LARGEUR, HAUTEUR, "Snake en Pyglet")

# --- Snake ---
snake = [(5, 5)]  # liste de positions (x, y)
direction = (1, 0)  # vers la droite
nouvelle_direction = direction

# --- Pomme ---
pomme = (10, 10)

# --- Dessin ---
def dessiner_case(x, y, couleur):
    return pyglet.shapes.Rectangle(
        x * TAILLE_CASE,
        y * TAILLE_CASE,
        TAILLE_CASE,
        TAILLE_CASE,
        color=couleur
    )

@window.event
def on_draw():
    window.clear()
    # Snake
    for (x, y) in snake:
        dessiner_case(x, y, (0, 200, 0)).draw()
    # Pomme
    dessiner_case(pomme[0], pomme[1], (200, 0, 0)).draw()

# --- Mouvements ---
def update(dt):
    global snake, pomme, direction, nouvelle_direction

    # Mettre à jour la direction (éviter demi-tour direct)
    if (nouvelle_direction[0] != -direction[0] or
        nouvelle_direction[1] != -direction[1]):
        direction = nouvelle_direction

    # Nouvelle tête
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Vérif collisions
    if (new_head in snake) or not (0 <= new_head[0] < NB_CASES_X) or not (0 <= new_head[1] < NB_CASES_Y):
        print("💀 Game Over!")
        pyglet.app.exit()
        return

    # Ajouter la tête
    snake.insert(0, new_head)

    # Vérif pomme
    if new_head == pomme:
        pomme = (random.randint(0, NB_CASES_X-1), random.randint(0, NB_CASES_Y-1))
    else:
        snake.pop()  # on supprime la queue si pas de pomme

# --- Clavier ---
@window.event
def on_key_press(symbol, modifiers):
    global nouvelle_direction
    if symbol == key.UP:
        nouvelle_direction = (0, 1)
    elif symbol == key.DOWN:
        nouvelle_direction = (0, -1)
    elif symbol == key.LEFT:
        nouvelle_direction = (-1, 0)
    elif symbol == key.RIGHT:
        nouvelle_direction = (1, 0)

# --- Lancement ---
pyglet.clock.schedule_interval(update, VITESSE)
pyglet.app.run()
