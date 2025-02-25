# Ajustar la posición de la barra de colores

También podemos ajustar la posición de la barra de colores utilizando `plt.axes`. Esta función toma una lista de valores `[izquierda, abajo, ancho, alto]` como argumentos para especificar la posición y el tamaño de los ejes. Ejecute el siguiente código:

```python
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
```
