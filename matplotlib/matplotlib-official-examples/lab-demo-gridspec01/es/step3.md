# Definir subtramas usando subplot2grid

Para definir subtramas usando `subplot2grid`, primero debemos especificar el tamaño de la cuadrícula usando una tupla con el número deseado de filas y columnas. También debemos especificar la ubicación de la subtrama dentro de la cuadrícula usando otra tupla.

Por ejemplo, para crear una cuadrícula 3x3 con una subtrama que abarque toda la primera fila y las tres columnas, usamos el siguiente código:

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
```

Para crear una subtrama que abarque la segunda fila y las dos primeras columnas, usamos:

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
```

Para crear una subtrama que abarque las dos últimas filas y la última columna, usamos:

```python
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
```

Para crear una subtrama en la última fila y la primera columna, usamos:

```python
ax4 = plt.subplot2grid((3, 3), (2, 0))
```

Para crear una subtrama en la última fila y la segunda columna, usamos:

```python
ax5 = plt.subplot2grid((3, 3), (2, 1))
```
