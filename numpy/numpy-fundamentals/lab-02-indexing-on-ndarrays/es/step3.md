# Corte y Avance

La indexación básica en NumPy extiende el concepto de indexación de Python a N dimensiones. Te permite seleccionar un rango de elementos a lo largo de cada dimensión de un array.

## Indexación Básica

La indexación básica ocurre cuando `obj` es un objeto de corte (construido por la notación `start:stop:step` dentro de corchetes), un entero o una tupla de objetos de corte y enteros.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])  # Salida: [1, 3, 5]
```

## Índices Negativos

Los índices negativos se pueden utilizar para indexar desde el final del array. Por ejemplo, `-1` se refiere al último elemento, `-2` se refiere al penúltimo elemento, y así sucesivamente.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[-2:10])  # Salida: [8, 9]
print(x[-3:3:-1])  # Salida: [7, 6, 5, 4]
```

## Valores Por Defecto para el Corte

Si no se especifica el índice de inicio, por defecto es 0 para valores de paso positivos y `-n-1` para valores de paso negativos. Si no se especifica el índice de parada, por defecto es `n` para valores de paso positivos y `-n-1` para valores de paso negativos. Si no se especifica el paso, por defecto es 1.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[5:])  # Salida: [5, 6, 7, 8, 9]
```
