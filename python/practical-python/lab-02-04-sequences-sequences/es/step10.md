# For y tuplas

Puedes iterar con múltiples variables de iteración.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Bucle con x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #           ...
```

Al usar múltiples variables, cada tupla se _desempaqueta_ en un conjunto de variables de iteración. La cantidad de variables debe coincidir con la cantidad de elementos en cada tupla.
