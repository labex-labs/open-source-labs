# Formatage du style C

Vous pouvez également utiliser l'opérateur de formatage `%`.

```python
>>> 'La valeur est %d' % 3
'La valeur est 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3,14'
```

Cela nécessite un seul élément ou un tuple à droite. Les codes de formatage sont également inspirés de `printf()` en C.

_Nota : C'est le seul formatage disponible pour les chaînes d'octets._

```python
>>> b'%s a %d messages' % (b'Dave', 37)
b'Dave a 37 messages'
>>> b'%b a %d messages' % (b'Dave', 37)  # %b peut être utilisé à la place de %s
b'Dave a 37 messages'
>>>
```
