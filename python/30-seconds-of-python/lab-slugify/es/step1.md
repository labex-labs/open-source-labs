# Cadena de texto a slug

Escribe una función `slugify(s)` que tome una cadena de texto `s` como argumento y devuelva un slug. La función debe realizar las siguientes operaciones:

1. Convertir la cadena de texto a minúsculas y eliminar cualquier espacio en blanco al principio o al final.
2. Reemplazar todos los caracteres especiales (es decir, cualquier carácter que no sea una letra, un dígito, un espacio en blanco, un guión o un subrayado) por una cadena de texto vacía.
3. Reemplazar todos los espacios en blanco, guiones y subrayados por un solo guión.
4. Eliminar cualquier guión al principio o al final.

```python
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```python
slugify('Hello World!') # 'hello-world'
```
