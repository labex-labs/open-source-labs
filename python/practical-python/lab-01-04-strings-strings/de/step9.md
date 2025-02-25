# Byte-Strings

Eine Zeichenkette von 8-Bit-Byte, die bei der niederen Ebene der I/O häufig vorkommt, wird wie folgt geschrieben:

```python
data = b'Hello World\r\n'
```

Indem Sie ein kleines b vor der ersten Anführungszeichen setzen, geben Sie an, dass es sich um eine Byte-Zeichenkette handelt, im Gegensatz zu einer Textzeichenkette.

Die meisten üblichen String-Operationen funktionieren.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

Das Indexieren ist etwas anders, da es Byte-Werte als Integer zurückgibt.

```python
data[0]   # 72 (ASCII-Code für 'H')
```

Konvertierung zu/aus Textzeichenketten.

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
```

Das Argument `'utf-8'` gibt eine Zeichensatzkodierung an. Andere übliche Werte sind `'ascii'` und `'latin1'`.
