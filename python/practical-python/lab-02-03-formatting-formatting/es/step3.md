# Formateo de diccionarios

Puedes usar el método `format_map()` para aplicar el formateo de cadenas a un diccionario de valores:

```python
>>> s = {
    'nombre': 'IBM',
    'acciones': 100,
    'precio': 91.1
}
>>> '{nombre:>10s} {acciones:10d} {precio:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

Utiliza los mismos códigos que `f-strings` pero toma los valores del diccionario suministrado.
