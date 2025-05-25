# Iterando sobre inteiros (Looping over integers)

Se você precisar contar, use `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

A sintaxe é `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Notice how it counts in steps of 2, not 1.
```

- O valor final nunca é incluído. Ele espelha o comportamento de fatias (slices).
- `start` é opcional. Padrão `0`.
- `step` é opcional. Padrão `1`.
- `range()` calcula os valores conforme necessário. Ele não armazena realmente uma grande faixa de números.
