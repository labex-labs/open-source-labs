# C-Style Formatierung

Sie können auch den Formatierungsoperator `%` verwenden.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

Dies erfordert einen einzelnen Wert oder ein Tupel auf der rechten Seite. Die Formatcodes sind ebenfalls nach der C `printf()` modelliert.

_Hinweis: Dies ist die einzige verfügbare Formatierung für Byte-Strings._

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b has %d messages' % (b'Dave', 37)  # %b kann anstelle von %s verwendet werden
b'Dave has 37 messages'
>>>
```
