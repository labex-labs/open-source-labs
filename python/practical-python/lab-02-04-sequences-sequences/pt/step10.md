# For e tuplas (tuples)

Você pode iterar com múltiplas variáveis de iteração.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Loops with x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #            ...
```

Ao usar múltiplas variáveis, cada tupla é _desempacotada_ (unpacked) em um conjunto de variáveis de iteração. O número de variáveis deve corresponder ao número de itens em cada tupla.
