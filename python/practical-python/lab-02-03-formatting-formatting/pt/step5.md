# Formatação no Estilo C

Você também pode usar o operador de formatação `%`.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

Isso requer um único item ou uma tupla à direita. Os códigos de formatação também são modelados após o `printf()` em C.

_Nota: Esta é a única formatação disponível em strings de bytes._

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b has %d messages' % (b'Dave', 37)  # %b may be used instead of %s
b'Dave has 37 messages'
>>>
```
