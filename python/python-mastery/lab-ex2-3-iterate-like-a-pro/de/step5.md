# Generator-Ausdrücke

Ein Generator-Ausdruck ist fast genau wie eine Listenkomprehension, nur dass er keine Liste erstellt. Stattdessen erstellt er ein Objekt, das die Ergebnisse schrittweise erzeugt - typischerweise für die Verarbeitung durch Iteration. Probieren Sie ein einfaches Beispiel:

```python
>>> nums = [1,2,3,4,5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x37caa8>
>>> for n in squares:
        print(n)

1
4
9
16
25
>>>
```

Sie werden feststellen, dass ein Generator-Ausdruck nur einmal verwendet werden kann. Schauen Sie, was passiert, wenn Sie die for-Schleife erneut ausführen:

```python
>>> for n in squares:
         print(n)

>>>
```

Sie können die Ergebnisse manuell nacheinander abrufen, indem Sie die `next()`-Funktion verwenden. Probieren Sie dies:

```python
>>> squares = (x*x for x in nums)
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
>>>
```

Halten Sie die Eingabe von `next()` fort, um zu sehen, was passiert, wenn keine weiteren Daten vorhanden sind.

Wenn die Aufgabe, die Sie ausführen, komplexer ist, können Sie immer noch von Generatoren profitieren, indem Sie eine Generatorfunktion schreiben und die `yield`-Anweisung verwenden. Beispielsweise:

```python
>>> def squares(nums):
        for x in nums:
            yield x*x

>>> for n in squares(nums):
        print(n)

1
4
9
16
25
>>>
```

Wir werden später im Kurs nochmals auf Generatorfunktionen zurückkommen - für jetzt betrachten Sie solche Funktionen einfach als solche, die das interessante Merkmal haben, Werte an die `for`-Anweisung zu liefern.
