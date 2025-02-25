# Bucle sobre enteros

Si necesitas contar, utiliza `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

La sintaxis es `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Observa cómo cuenta de 2 en 2, no de 1 en 1.
```

- El valor final nunca se incluye. Imita el comportamiento de los rebanados.
- `start` es opcional. Valor predeterminado `0`.
- `step` es opcional. Valor predeterminado `1`.
- `range()` calcula los valores según sea necesario. No almacena realmente una gran cantidad de números.
