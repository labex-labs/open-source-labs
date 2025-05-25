# Personalizar a seta para conectar à elipse

Nesta etapa, personalizaremos a seta para conectar à elipse. Usaremos o parâmetro `arrowprops` para especificar que a seta deve se conectar à elipse e também personalizaremos o estilo e a cor da seta.

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
