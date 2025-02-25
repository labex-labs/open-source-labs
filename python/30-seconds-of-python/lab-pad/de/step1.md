# String auffüllen

Schreiben Sie eine Funktion `pad(s: str, length: int, char: str = ' ') -> str`, die einen String auf beiden Seiten mit dem angegebenen Zeichen auffüllt, wenn er kürzer als die angegebene Länge ist. Die Funktion sollte drei Parameter entgegennehmen:

- `s`: ein String, der aufgefüllt werden muss
- `length`: eine Ganzzahl, die die Gesamtlänge des aufgefüllten Strings angibt
- `char`: ein Zeichen, das zum Auffüllen des Strings verwendet wird. Der Standardwert ist ein Leerzeichen.

Die Funktion sollte den aufgefüllten String zurückgeben.

```python
from math import floor

def pad(s, length, char = ' '):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```python
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
