# Agregando anotaciones a la gráfica

Podemos agregar anotaciones a la gráfica utilizando la función `ax.annotate()`. Esta función toma tres argumentos: el texto de la anotación, la coordenada xy del punto a anotar y la coordenada xy de la posición del texto. Podemos personalizar el estilo de la anotación utilizando el argumento `arrowprops`.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
