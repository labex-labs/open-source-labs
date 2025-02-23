# Personalizar la flecha para que se contraiga hacia la elipse

En este paso, personalizaremos la flecha para que se contraiga hacia la elipse. Utilizaremos el parámetro `shrinkB` para especificar la cantidad por la que la flecha debe contraerse hacia la elipse.

```python
ax = axs.flat[3]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="fancy",
                            color="0.5",
                            patchB=el,
                            shrinkB=5,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
