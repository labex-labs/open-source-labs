# Agregando texto a la gráfica

Podemos agregar texto a la gráfica utilizando la función `ax.text()`. Esta función toma tres argumentos: la coordenada x, la coordenada y y la cadena de texto. Podemos personalizar el estilo del texto utilizando los argumentos `style`, `bbox` y `fontsize`.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```
