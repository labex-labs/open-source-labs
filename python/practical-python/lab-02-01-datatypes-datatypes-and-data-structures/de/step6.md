# Tupel-Aufpacken

Um das Tupel an einem anderen Ort zu verwenden, können Sie seine Teile in Variablen aufpacken.

```python
name, shares, price = s
print('Cost', shares * price)
```

Die Anzahl der Variablen auf der linken Seite muss der Tupelstruktur entsprechen.

```python
name, shares = s     # FEHLER
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
