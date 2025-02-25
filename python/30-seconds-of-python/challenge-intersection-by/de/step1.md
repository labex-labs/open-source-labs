# Listeinschnitt basierend auf Funktion

## Problemstellung

Schreiben Sie eine Funktion `intersection_by(a, b, fn)`, die zwei Listen `a` und `b` sowie eine Funktion `fn` als Parameter erhält. Die Funktion sollte eine Liste von Elementen zurückgeben, die in beiden Listen vorhanden sind, nachdem die bereitgestellte Funktion auf jedes Listenelement beider Listen angewendet wurde.

### Eingabe

- Zwei Listen `a` und `b` (1 <= len(a), len(b) <= 1000)
- Eine Funktion `fn`, die einen Parameter annimmt und einen Wert zurückgibt

### Ausgabe

- Eine Liste von Elementen, die in beiden Listen vorhanden sind, nachdem die bereitgestellte Funktion auf jedes Listenelement beider Listen angewendet wurde.

## Beispiel

```python
intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```

### Hinweis

Im obigen Beispiel wird die Funktion `floor()` auf jedes Element in beiden Listen angewendet. Die resultierenden Mengen sind `{2, 3}` und `{2, 1}`. Die Schnittmenge dieser Mengen ist `{2}`, die dann als Liste zurückgegeben wird.
