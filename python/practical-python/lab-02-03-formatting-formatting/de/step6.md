# Übung 2.8: Wie man Zahlen formatiert

Ein häufiges Problem bei der Ausgabe von Zahlen ist die Angabe der Anzahl der Nachkommastellen. Eine Möglichkeit, dieses Problem zu beheben, ist die Verwendung von f-Strings. Probieren Sie diese Beispiele aus:

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```

Die vollständige Dokumentation zu den im f-Strings verwendeten Formatcodes finden Sie [hier](https://docs.python.org/3/library/string.html#format-specification-mini-language). Die Formatierung wird manchmal auch mit dem `%-Operator` von Zeichenketten durchgeführt.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

Die Dokumentation zu den verschiedenen Codes, die mit `%` verwendet werden, finden Sie [hier](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Obwohl es üblicherweise mit `print` verwendet wird, ist die Zeichenkettenformatierung nicht an das Ausgeben gebunden. Wenn Sie eine formattierte Zeichenkette speichern möchten, weisen Sie sie einfach einer Variablen zu.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```
