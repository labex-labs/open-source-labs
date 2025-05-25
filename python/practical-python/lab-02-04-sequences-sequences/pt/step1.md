# Tipos de Dados de Sequência (Sequence Datatypes)

Python possui três tipos de dados de _sequência_ (sequence).

- String: `'Hello'`. Uma string é uma sequência de caracteres.
- List: `[1, 4, 5]`.
- Tuple: `('GOOG', 100, 490.1)`.

Todas as sequências são ordenadas, indexadas por inteiros e possuem um comprimento.

```python
a = 'Hello'               # String
b = [1, 4, 5]             # List
c = ('GOOG', 100, 490.1)  # Tuple

# Ordem indexada
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Comprimento da sequência
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Sequências podem ser replicadas: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequências do mesmo tipo podem ser concatenadas: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```
