# Liste summieren basierend auf einer Funktion

## Problemstellung

Schreiben Sie eine Funktion `sum_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte jedes Element der Liste mithilfe der bereitgestellten Funktion auf einen Wert abbilden und die Summe der Werte zurückgeben.

## Beispiel

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

Im obigen Beispiel nimmt die `sum_by()`-Funktion eine Liste von Wörterbüchern und eine Lambda-Funktion entgegen, die den Wert des `'n'`-Schlüssels aus jedem Wörterbuch extrahiert. Die Funktion bildet jedes Wörterbuch auf seinen `'n'`-Wert ab und gibt die Summe der Werte zurück, was `20` ist.
