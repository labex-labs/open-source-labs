# Crear un gráfico con escala logit

El cuarto tipo de transformación de escala que exploraremos es la logit. Este tipo de escala es útil cuando se tratan datos que están limitados entre 0 y 1. Para crear un gráfico con escala logit, usamos el método `set_yscale()` y le pasamos la cadena `'logit'`. También agregamos un título y una cuadrícula al gráfico.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
