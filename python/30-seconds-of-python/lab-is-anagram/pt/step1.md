# Anagrama de String (String Anagram)

Escreva uma função `is_anagram(s1, s2)` que recebe duas strings como argumentos e retorna `True` se elas são anagramas uma da outra, e `False` caso contrário. A função deve ser _case-insensitive_ (não sensível a maiúsculas e minúsculas), ignorar espaços, pontuação e caracteres especiais.

Para resolver este problema, você pode seguir estes passos:

1.  Use `str.isalnum()` para filtrar caracteres não alfanuméricos e `str.lower()` para transformar cada caractere em minúsculas.
2.  Use `collections.Counter` para contar os caracteres resultantes para cada string e comparar os resultados.

```python
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

```python
is_anagram('#anagram', 'Nag a ram!')  # True
```
