# Más ejemplos de sistemas de coordenadas

A continuación mostraremos algunos más ejemplos de sistemas de coordenadas y cómo se puede especificar la ubicación de las anotaciones.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)

bbox_args = dict(boxstyle="round", fc="0.8")
arrow_args = dict(arrowstyle="->")

# Aquí demostraremos los límites del sistema de coordenadas y cómo
# colocamos el texto de las anotaciones.

ax1.annotate('fracción de figura : 0, 0', xy=(0, 0), xycoords='fracción de figura',
             xytext=(20, 20), textcoords='puntos de desplazamiento',
             ha="left", va="bottom",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax1.annotate('fracción de figura : 1, 1', xy=(1, 1), xycoords='fracción de figura',
             xytext=(-20, -20), textcoords='puntos de desplazamiento',
             ha="right", va="top",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax1.annotate('fracción de eje : 0, 0', xy=(0, 0), xycoords='fracción de eje',
             xytext=(20, 20), textcoords='puntos de desplazamiento',
             ha="left", va="bottom",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax1.annotate('fracción de eje : 1, 1', xy=(1, 1), xycoords='fracción de eje',
             xytext=(-20, -20), textcoords='puntos de desplazamiento',
             ha="right", va="top",
             bbox=bbox_args,
             arrowprops=arrow_args)

# También es posible generar anotaciones arrastrables

an1 = ax1.annotate('Arrastrame 1', xy=(.5,.7), xycoords='data',
                   ha="center", va="center",
                   bbox=bbox_args)

an2 = ax1.annotate('Arrastrame 2', xy=(.5,.5), xycoords=an1,
                   xytext=(.5,.3), textcoords='fracción de eje',
                   ha="center", va="center",
                   bbox=bbox_args,
                   arrowprops=dict(patchB=an1.get_bbox_patch(),
                                   connectionstyle="arc3,rad=0.2",
                                   **arrow_args))
an1.draggable()
an2.draggable()

an3 = ax1.annotate('', xy=(.5,.5), xycoords=an2,
                   xytext=(.5,.5), textcoords=an1,
                   ha="center", va="center",
                   bbox=bbox_args,
                   arrowprops=dict(patchA=an1.get_bbox_patch(),
                                   patchB=an2.get_bbox_patch(),
                                   connectionstyle="arc3,rad=0.2",
                                   **arrow_args))

# Finalmente mostraremos algunas anotaciones y colocaciones más complejas

text = ax2.annotate('xy=(0, 1)\nxycoords=("data", "fracción de eje")',
                    xy=(0, 1), xycoords=("data", 'fracción de eje'),
                    xytext=(0, -20), textcoords='puntos de desplazamiento',
                    ha="center", va="top",
                    bbox=bbox_args,
                    arrowprops=arrow_args)

ax2.annotate('xy=(0.5, 0)\nxycoords=artista',
             xy=(0.5, 0.), xycoords=text,
             xytext=(0, -20), textcoords='puntos de desplazamiento',
             ha="center", va="top",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax2.annotate('xy=(0.8, 0.5)\nxycoords=ax1.transData',
             xy=(0.8, 0.5), xycoords=ax1.transData,
             xytext=(10, 10),
             textcoords=OffsetFrom(ax2.bbox, (0, 0), "points"),
             ha="left", va="bottom",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax2.set(xlim=[-2, 2], ylim=[-2, 2])
```
