# Personalizar las espinas para los lados inferior y izquierdo

En el segundo subgráfico, mostraremos las espinas solo en los lados inferior e izquierdo de la gráfica. Podemos ocultar las espinas en los lados derecho y superior de la gráfica utilizando el método `set_visible`.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
