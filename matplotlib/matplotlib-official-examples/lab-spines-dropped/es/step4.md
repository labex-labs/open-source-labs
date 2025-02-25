# Desplazar las espinas

Moveremos las espinas izquierda y inferior hacia afuera 10 puntos utilizando la función `set_position()`. El argumento para `set_position()` es una tupla con dos elementos. El primer elemento representa la posición de la espina y el segundo elemento representa la distancia desde la espina hasta el área de la gráfica.

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
