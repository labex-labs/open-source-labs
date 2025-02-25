# Asignación de Valores a Arrays Indexados

Puedes asignar valores a elementos específicos o subconjuntos de elementos en un array utilizando indexación. El valor que se está asignando debe ser de forma consistente con el array indexado.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Salida: [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Salida: [0, 1, 0, 1, 2, 3, 7, 8, 9]
```
