# Formatear la gráfica

Para que nuestra gráfica sea más legible, podemos formatearla utilizando las funciones de formato de Matplotlib. En este ejemplo, formatearemos las etiquetas del eje y para que muestren los valores en millones.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
