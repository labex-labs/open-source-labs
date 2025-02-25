# Personalizar las anotaciones

Podemos personalizar las anotaciones cambiando el tamaño de fuente, el color de fuente y el estilo de flecha. El siguiente código cambiará el tamaño de fuente, el color de fuente y el estilo de flecha de la anotación de texto.

```python
ax.annotate("Punto de datos 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```
