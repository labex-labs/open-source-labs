# Indexação de String

Strings funcionam como um array para acessar caracteres individuais. Você usa um índice inteiro, começando em 0. Índices negativos especificam uma posição relativa ao final da string.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (end of string)
```

Você também pode fatiar (slice) ou selecionar substrings especificando um intervalo de índices com `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

O caractere no índice final não está incluído. Índices ausentes assumem o início ou o fim da string.
