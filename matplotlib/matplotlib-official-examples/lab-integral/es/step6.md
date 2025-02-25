# Agregar la etiqueta de la integral

Agrega la etiqueta de la integral a la gráfica utilizando `text`. La etiqueta debe estar centrada en el punto medio entre a y b y debe formatearse utilizando mathtext.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
