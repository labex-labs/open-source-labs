# Selección simple, líneas, rectángulos y texto

Comenzaremos habilitando la selección simple estableciendo la propiedad "picker" de un artista. Esto permitirá que el artista lance un evento de selección si el evento del mouse se encuentra sobre el artista. Crearemos una trama simple que contenga una línea, un rectángulo y texto, y habilitaremos la selección en cada uno de estos artistas.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Pick the rectangle.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Make the xtick labels pickable.
    label.set_picker(True)
```
