# Упражнение 1.24: Собираем все вместе

Хотите взять список строк и объединить их в одну строку? Используйте метод `join()` для строк так (заметьте: сначала это выглядит странно).

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
