# f-Strings

Eine Zeichenkette mit formatierter Ausdruckssubstitution.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

**Hinweis: Dies erfordert Python 3.6 oder neuer.** Die Bedeutung der Formatcodes wird später behandelt.

In diesen Übungen werden Sie mit Operationen auf Python's String-Typ experimentieren. Sie sollten dies an der Python interaktiven Eingabeaufforderung machen, wo Sie die Ergebnisse leicht sehen können. Wichtiger Hinweis:

> In Übungen, in denen Sie mit dem Interpreter interagieren sollen, ist `>>>` der Interpreter-Prompt, den Sie erhalten, wenn Python Sie auffordert, eine neue Anweisung einzugeben. Einige Anweisungen in der Übung umfassen mehrere Zeilen - um diese Anweisungen auszuführen, müssen Sie möglicherweise einige Male 'Return' drücken. Ein erneuter Hinweis: Sie _TIppen NICHT_ das `>>>` ein, wenn Sie diese Beispiele ausprobieren.

Beginnen Sie mit der Definition einer Zeichenkette, die eine Reihe von Aktiensymbole enthält, wie folgt:

```python
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```
