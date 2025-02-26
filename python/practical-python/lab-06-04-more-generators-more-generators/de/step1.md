# Generatorausdrücke

Eine Generator-Version einer List Comprehension.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

Unterschiede zu List Comprehensions:

- Konstruiert keine Liste.
- Einziges nützliches Ziel ist die Iteration.
- Einmal verbraucht, kann nicht wiederverwendet werden.

Allgemeine Syntax:

```python
(<expression> for i in s if <conditional>)
```

Es kann auch als Funktionsargument dienen.

```python
sum(x*x for x in a)
```

Es kann auf jedes Iterable angewendet werden.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

Der Hauptgebrauch von Generatorausdrücken liegt in Code, der eine Berechnung auf einer Sequenz durchführt, aber das Ergebnis nur einmal verwendet. Beispielsweise werden alle Kommentare aus einer Datei entfernt.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
  ...
f.close()
```

Mit Generatoren läuft der Code schneller und verwendet wenig Speicher. Es ist wie ein Filter, der auf einem Stream angewendet wird.
