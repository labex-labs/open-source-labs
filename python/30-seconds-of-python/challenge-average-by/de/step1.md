# Mittelwert einer abgebildeten Liste

## Problemstellung

Schreiben Sie eine Funktion namens `average_by(lst, fn = lambda x: x)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion `fn` sollte verwendet werden, um jedes Element der Liste auf einen Wert abzubilden. Die Funktion sollte dann den Mittelwert der abgebildeten Werte berechnen und zurückgeben.

Wenn das Argument `fn` nicht angegeben wird, sollte die Funktion die Standardidentitätsfunktion verwenden, die einfach das Element selbst zurückgibt.

Ihre Funktion sollte die folgenden Anforderungen erfüllen:

- Verwenden Sie `map()`, um jedes Element auf den von `fn` zurückgegebenen Wert abzubilden.
- Verwenden Sie `sum()`, um alle abgebildeten Werte zu summieren und dividieren Sie durch `len(lst)`.
- Lassen Sie das letzte Argument `fn` weg, um die Standardidentitätsfunktion zu verwenden.

Funktionssignatur: `def average_by(lst, fn = lambda x: x) -> float:`

## Beispiel

```python
assert average_by([1, 2, 3, 4, 5]) == 3.0
assert average_by([1, 2, 3, 4, 5], lambda x: x**2) == 11.0
assert average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']) == 5.0
```
