# Indexación Básica

Los arrays de NumPy se pueden indexar utilizando la sintaxis estándar de Python `x[obj]`, donde `x` es el array y `obj` es la selección. Hay diferentes tipos de indexación disponibles dependiendo del tipo de `obj`.

## Indexación de Un Solo Elemento

La indexación de un solo elemento funciona exactamente igual que la indexación para otras secuencias estándar de Python. Es basada en 0 y acepta índices negativos para indexar desde el final del array.

```python
x = np.arange(10)
print(x[2])  # Salida: 2
print(x[-2])  # Salida: 8
```

## Indexación Multidimensional

Los arrays pueden tener múltiples dimensiones, y la indexación funciona de la misma manera para cada dimensión. Puedes acceder a los elementos en un array multidimensional separando el índice de cada dimensión con una coma.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Salida: 8
print(x[1, -1])  # Salida: 9
```

## Indexación de Array Subdimensional

Si indexas un array multidimensional con menos índices que dimensiones, obtienes un array subdimensional. Cada índice especificado selecciona el array correspondiente al resto de las dimensiones seleccionadas.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Salida: [0, 1, 2, 3, 4]
```
