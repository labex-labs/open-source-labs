# Formateo estilo C

También puedes usar el operador de formateo `%`.

```python
>>> 'El valor es %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

Esto requiere un solo elemento o una tupla en el lado derecho. Los códigos de formato también se basan en `printf()` de C.

_Nota: Este es el único formateo disponible para cadenas de bytes._

```python
>>> b'%s tiene %d mensajes' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b tiene %d mensajes' % (b'Dave', 37)  # %b puede usarse en lugar de %s
b'Dave has 37 messages'
>>>
```
