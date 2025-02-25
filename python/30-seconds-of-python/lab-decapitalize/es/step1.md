# Convertir la primera letra de una cadena a minúscula

Escribe una función `decapitalize(s, upper_rest = False)` que tome una cadena `s` y devuelva una nueva cadena con la primera letra en minúscula. La función también debe tener un parámetro opcional `upper_rest` que, cuando se establece en `True`, convertirá el resto de la cadena a mayúsculas.

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
