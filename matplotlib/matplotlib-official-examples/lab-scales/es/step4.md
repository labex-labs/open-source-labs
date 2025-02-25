# Crear un gráfico con escala logarítmica simétrica

El tercer tipo de transformación de escala que exploraremos es la logarítmica simétrica. Este tipo de escala es útil cuando se tratan datos que contienen valores positivos y negativos. Para crear un gráfico con escala logarítmica simétrica, usamos el método `set_yscale()` y le pasamos la cadena `'symlog'`. También establecemos el parámetro `linthresh` en `0.02` para especificar el rango de valores alrededor de cero que se escalarán linealmente. También agregamos un título y una cuadrícula al gráfico.

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
