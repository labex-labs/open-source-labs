# Maximum-Wert in einer Liste basierend auf einer Funktion finden

## Problemstellung

Schreiben Sie eine Funktion `max_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte jedes Element in `lst` mithilfe der bereitgestellten Funktion `fn` auf einen Wert abbilden und dann den maximalen Wert zurückgeben.

## Beispiel

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```

## Beschränkungen

- Die Liste `lst` enthält mindestens ein Element.
- Die Funktion `fn` nimmt ein Argument und gibt einen Wert zurück.
