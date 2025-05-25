# Palíndromo

Escreva uma função `palindrome(s)` que recebe uma string `s` como seu único parâmetro e retorna `True` se `s` for um palíndromo e `False` caso contrário. Sua função deve ignorar a capitalização e os caracteres não alfanuméricos ao verificar palíndromos.

Para resolver este problema, você pode seguir estes passos:

1. Use `str.lower()` para converter a string para minúsculas.
2. Use `re.sub()` para remover todos os caracteres não alfanuméricos da string.
3. Compare a string resultante com sua versão invertida usando a notação de fatiamento (slice notation).

```python
from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]
```

```python
palindrome('taco cat') # True
```
