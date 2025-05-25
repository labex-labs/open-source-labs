# Exercício 1.13: Extraindo caracteres individuais e substrings

Strings são arrays de caracteres. Tente extrair alguns caracteres:

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Last character
?
>>> symbols[-2]        # Negative indices are from end of string
?
>>>
```

Em Python, strings são somente leitura (read-only).

Verifique isso tentando mudar o primeiro caractere de `symbols` para um 'a' minúsculo.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
