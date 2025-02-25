# Crear un trazado simple

Para crear un trazado simple en Matplotlib, debe proporcionar una lista de números que desea trazar. En este caso, trazaremos una lista de números en función de su índice, lo que resultará en una línea recta. Utilice una cadena de formato (aquí, 'o-r') para establecer los marcadores (círculos), el estilo de línea (línea sólida) y el color (rojo).

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('algunos números')
plt.show()
```
