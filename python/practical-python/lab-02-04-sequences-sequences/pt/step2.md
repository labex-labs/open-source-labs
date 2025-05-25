# Fatiamento (Slicing)

Fatiamento (Slicing) significa obter uma subsequência de uma sequência. A sintaxe é `s[start:end]`. Onde `start` e `end` são os índices da subsequência desejada.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

- Os índices `start` e `end` devem ser inteiros.
- Fatias (Slices) _não_ incluem o valor final. É como um intervalo semiaberto da matemática.
- Se os índices forem omitidos, eles assumem o padrão do início ou do fim da lista.
