# Desafío de Anagramas de Cadenas

## Problema

Escribe una función `is_anagram(s1, s2)` que tome dos cadenas como argumentos y devuelva `True` si son anagramas la una de la otra, y `False` en caso contrario. La función debe ser insensible a mayúsculas y minúsculas, ignorar espacios, signos de puntuación y caracteres especiales.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `str.isalnum()` para filtrar los caracteres no alfanuméricos y `str.lower()` para transformar cada carácter a minúsculas.
2. Utiliza `collections.Counter` para contar los caracteres resultantes de cada cadena y comparar los resultados.

## Ejemplo

```python
is_anagram('#anagram', 'Nag a ram!')  # True
is_anagram('hello', 'world')  # False
```
