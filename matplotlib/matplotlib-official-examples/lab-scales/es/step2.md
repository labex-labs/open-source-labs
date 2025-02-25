# Crear un gráfico con escala lineal

El primer tipo de transformación de escala que exploraremos es la lineal. Esta es la escala predeterminada utilizada en Matplotlib. Para crear un gráfico con escala lineal, usamos el método `set_yscale()` y le pasamos la cadena `'linear'`. También agregamos un título y una cuadrícula al gráfico.

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
