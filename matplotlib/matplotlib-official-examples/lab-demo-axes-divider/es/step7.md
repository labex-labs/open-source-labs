# Graficado

En este paso, crearemos una figura y agregaremos subgráficos para cada imagen que queramos crear.

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # GRAFICA 1
    # imagen simple y barra de color
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # GRAFICA 2
    # imagen y barra de color con posicionamiento en tiempo de dibujo: una forma difícil
    demo_locatable_axes_hard(fig)

    # GRAFICA 3
    # imagen y barra de color con posicionamiento en tiempo de dibujo: una forma fácil
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # GRAFICA 4
    # dos imágenes una al lado de la otra con relleno fijo.
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```
