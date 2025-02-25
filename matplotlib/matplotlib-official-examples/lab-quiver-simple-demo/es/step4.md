# Crear la clave de flechas

Podemos agregar una clave de flechas al gráfico para mostrar la escala de las flechas. Usamos la función `ax.quiverkey()` para agregar la clave. Pasamos el objeto `q`, la posición `X` e `Y` de la clave, la longitud de la flecha, la etiqueta para la clave y la posición de la etiqueta.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Clave de flechas, longitud = 10', labelpos='E')
```
