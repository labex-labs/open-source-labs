# Finde den kleinsten Wert einer Liste basierend auf einer Funktion

## Problemstellung

Schreibe eine Funktion namens `min_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente erhält. Die Funktion sollte jedes Element in der Liste mithilfe der bereitgestellten Funktion zu einem Wert abbilden und dann den kleinsten Wert zurückgeben.

## Beispiel

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```

Im obigen Beispiel wird die `min_by()`-Funktion mit einer Liste von Wörterbüchern und einer Lambda-Funktion aufgerufen, die den Wert des `'n'`-Schlüssels aus jedem Wörterbuch extrahiert. Die Funktion gibt den kleinsten Wert der Liste zurück, der `2` ist.
