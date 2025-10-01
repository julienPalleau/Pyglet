# https://www.youtube.com/watch?v=GMUhXMw1zZE

import pyglet
from pyglet import shapes

# Créer une fenêtre
window = pyglet.window.Window(width=1280, height=720, caption="Hello Pyglet")
window.set_location(x=400, y=200)

# Créer un batch pour le dessin
batch = pyglet.graphics.Batch()

circle1 = shapes.Circle(x=700, y=150, radius=100, color=(50, 225, 30), batch=batch)
circle2 = shapes.Arc(x=250, y=250, radius=100, color=(255, 0, 0), thickness=2, batch=batch)
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255), batch=batch)
rectangle = shapes.Rectangle(x=250, y=300, width=400, height=200, color=(255, 22, 20), batch=batch)
rectangle.opacity=100


@window.event
def on_draw() -> None:
    window.clear()
    batch.draw()

pyglet.app.run()