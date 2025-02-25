# String-Indexierung

Strings funktionieren wie ein Array für den Zugriff auf einzelne Zeichen. Sie verwenden einen ganzzahligen Index, der bei 0 beginnt. Negative Indizes geben eine Position relativ zum Ende der Zeichenkette an.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (Ende der Zeichenkette)
```

Sie können auch Teile oder Substrings auswählen, indem Sie einen Bereich von Indizes mit `:` angeben.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

Das Zeichen am Endindex ist nicht enthalten. Fehlende Indizes nehmen den Anfang oder das Ende der Zeichenkette an.
