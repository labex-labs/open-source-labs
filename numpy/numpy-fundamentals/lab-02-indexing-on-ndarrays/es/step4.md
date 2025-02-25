# Indexación Avanzada

La indexación avanzada se activa cuando el objeto de selección `obj` es un objeto de secuencia no tupla, una ndarray (de tipo de datos entero o booleano) o una tupla con al menos un objeto de secuencia o ndarray (de tipo de datos entero o booleano). Hay dos tipos de indexación avanzada: entera y booleana.

## Indexación de Array Entero

La indexación de array entero permite la selección de elementos arbitrarios en el array basados en su índice N-dimensional. Cada array entero representa una cantidad de índices en esa dimensión.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Salida: [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Salida: [7, 7, 4, 2]
```

## Indexación de Array Booleano

La indexación de array booleano permite la selección de elementos del array basados en una condición booleana. El resultado es un nuevo array que contiene solo los elementos correspondientes a los valores `True` del array booleano.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Salida: [ 1., 19., 18., 3.]
```
