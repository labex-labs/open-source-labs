# Método format()

Existe un método `format()` que puede aplicar formateo a argumentos posicionales o argumentos de palabras clave.

```python
>>> '{nombre:>10s} {acciones:10d} {precio:10.2f}'.format(nombre='IBM', acciones=100, precio=91.1)
'       IBM        100      91.10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

Para ser franco, `format()` es un poco verboso. Prefiero `f-strings`.
