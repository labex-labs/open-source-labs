# Rellenar número

Escribe una función `pad_number(n, l)` que tome un número `n` y una longitud `l` y devuelva una cadena que represente el número rellenado. La función debe rellenar el número con ceros a la izquierda para que tenga `l` dígitos de longitud. Si el número ya tiene `l` dígitos de longitud, la función debe devolver el número como una cadena.

Para rellenar el número, puedes usar el método `str.zfill()`. Este método toma una longitud y rellena la cadena con ceros a la izquierda hasta que tenga esa longitud. Por ejemplo, `"7".zfill(6)` devolvería `"000007"`.

```python
def pad_number(n, l):
  return str(n).zfill(l)
```

```python
pad_number(1234, 6); # '001234'
```
