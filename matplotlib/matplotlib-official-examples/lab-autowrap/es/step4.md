# Controlar la colocación y el estilo del texto

También podemos controlar la colocación y el estilo del texto en nuestra gráfica de Matplotlib. Intente agregar el siguiente código a su script:

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

Esto agregará cuatro elementos de texto a nuestra gráfica, cada uno con un color, tamaño de fuente y posición diferentes.
