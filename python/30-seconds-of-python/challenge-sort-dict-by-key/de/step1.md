# Wörterbuch nach Schlüssel sortieren

## Problemstellung

Schreiben Sie eine Funktion `sort_dict_by_key(d, reverse=False)`, die ein Wörterbuch `d` annimmt und ein neues, nach Schlüssel sortiertes Wörterbuch zurückgibt. Die Funktion sollte einen optionalen Parameter `reverse` haben, der standardmäßig `False` ist. Wenn `reverse` `True` ist, sollte das Wörterbuch in umgekehrter Reihenfolge sortiert werden.

## Beispiel

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True) # {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
