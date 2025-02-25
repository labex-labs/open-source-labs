# Exercice 1.24 : Remettre tout en place

Voulez prendre une liste de chaînes de caractères et les joindre pour former une seule chaîne? Utilisez la méthode `join()` des chaînes de caractères comme ceci (note : cela semble étrange au premier abord).

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
