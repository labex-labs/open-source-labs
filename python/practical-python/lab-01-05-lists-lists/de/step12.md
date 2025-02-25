# Übung 1.24: Alles wieder zusammenbringen

Möchten Sie eine Liste von Zeichenketten zu einer einzigen Zeichenkette zusammenfügen? Verwenden Sie die `join()`-Methode von Zeichenketten wie folgt (Hinweis: Dies sieht zunächst komisch aus).

```python
>>> a = ','.join(symlist)
>>> a
'YHOO,RHT,HPQ,GOOG,AIG,AAPL,AA'
>>> b = ':'.join(symlist)
>>> b
'YHOO:RHT:HPQ:GOOG:AIG:AAPL:AA'
>>> c = ''.join(symlist)
>>> c
'YHOORHTHPQGOOGAIGAAPLAA'
>>>
```
