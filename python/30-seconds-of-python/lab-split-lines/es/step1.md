# Dividir en líneas

Escribe una función llamada `split_lines(s)` que tome una cadena de texto multilínea `s` como entrada y devuelva una lista de líneas individuales. Tu función debe dividir la cadena en cada salto de línea (`\n`) y devolver una lista de las líneas resultantes.

```python
def split_lines(s):
  return s.split('\n')
```

```python
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a','multiline','string.', '']
```
