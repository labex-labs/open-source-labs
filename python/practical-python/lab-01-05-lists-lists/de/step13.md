# Übung 1.25: Listen von beliebigen Objekten

Listen können beliebige Arten von Objekten enthalten, einschließlich anderer Listen (z.B. geschachtelte Listen). Testen Sie dies:

```python
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Achten Sie genau auf die obige Ausgabe. `items` ist eine Liste mit drei Elementen. Das erste Element ist eine Zeichenkette, aber die anderen beiden Elemente sind Listen.

Sie können auf Elemente in den geschachtelten Listen über mehrere Indexoperationen zugreifen.

```python
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

Auch wenn es technisch möglich ist, sehr komplizierte Listenstrukturen zu erstellen, sollten Sie als allgemeine Regel die Dinge einfach halten. Normalerweise halten Listen Elemente, die alle vom gleichen Wertetyp sind. Beispielsweise eine Liste, die ausschließlich aus Zahlen besteht, oder eine Liste von Textzeichenketten. Das Mischen unterschiedlicher Datentypen in derselben Liste ist oft ein guter Weg, um sich den Kopf zu verbluten, daher ist es am besten zu vermeiden.
