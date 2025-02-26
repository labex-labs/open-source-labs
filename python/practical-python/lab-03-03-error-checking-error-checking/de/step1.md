# Wie Programme fehlschlagen

Python führt keine Prüfung oder Validierung der Typen oder Werte von Funktionsargumenten durch. Eine Funktion funktioniert mit beliebigen Daten, die mit den Anweisungen in der Funktion kompatibel sind.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

Wenn in einer Funktion Fehler auftreten, erscheinen sie zur Laufzeit (als Ausnahme).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

Um den Code zu überprüfen, liegt ein starker Schwerpunkt auf der Tests (siehe später).
