# Palíndromo

## Problema

Escribe una función `palindrome(s)` que tome una cadena `s` como único parámetro y devuelva `True` si `s` es un palíndromo y `False` en caso contrario. Tu función debe ignorar la capitalización y los caracteres no alfanuméricos al comprobar si es un palíndromo.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `str.lower()` para convertir la cadena a minúsculas.
2. Utiliza `re.sub()` para eliminar todos los caracteres no alfanuméricos de la cadena.
3. Compara la cadena resultante con su inversa utilizando notación de rebanadas.

## Ejemplo

```python
palindrome('taco cat') # True
palindrome('A man, a plan, a canal: Panama') # True
palindrome('hello world') # False
```
