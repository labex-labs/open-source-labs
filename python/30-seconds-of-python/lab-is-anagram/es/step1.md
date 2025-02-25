# Anagrama de cadenas

Escribe una función `is_anagram(s1, s2)` que tome dos cadenas como argumentos y devuelva `True` si son anagramas una de la otra, y `False` en caso contrario. La función debe ser insensible a mayúsculas y minúsculas, ignorar espacios, signos de puntuación y caracteres especiales.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `str.isalnum()` para filtrar los caracteres no alfanuméricos y `str.lower()` para transformar cada carácter a minúsculas.
2. Utiliza `collections.Counter` para contar los caracteres resultantes de cada cadena y comparar los resultados.

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
