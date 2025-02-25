# Capitalizar Cadena

Escribe una función de Python llamada `capitalize_string(s, lower_rest=False)` que tome una cadena de texto como argumento y devuelva una nueva cadena con la primera letra en mayúscula. La función debe tener un parámetro opcional `lower_rest` que, si se establece en `True`, convierte el resto de la cadena a minúsculas.

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
