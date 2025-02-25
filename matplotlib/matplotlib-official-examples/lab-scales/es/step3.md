# Crear un gráfico con escala logarítmica

El siguiente tipo de transformación de escala que exploraremos es la logarítmica. Para crear un gráfico con escala logarítmica, usamos el método `set_yscale()` y le pasamos la cadena `'log'`. También agregamos un título y una cuadrícula al gráfico.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
