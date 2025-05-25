# Reatribuição de valores

Reatribuir um valor _nunca_ sobrescreve a memória usada pelo valor anterior.

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]    Holds the original value
```

Lembre-se: **Variáveis são nomes, não localizações de memória.**
