# Funktionen zusammensetzen

## Problemstellung

Schreiben Sie eine Funktion namens `compose(*fns)`, die eine oder mehrere Funktionen als Argumente akzeptiert und eine neue Funktion zurückgibt, die das Ergebnis der Komposition der Eingabefunktionen von rechts nach links ist. Die letzte (rechtsmöglichste) Funktion kann ein oder mehrere Argumente akzeptieren; die verbleibenden Funktionen müssen einstellige sein.

## Beispiel

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```

Im obigen Beispiel definieren wir zwei Funktionen `add5` und `multiply`. Anschließend verwenden wir die `compose()`-Funktion, um eine neue Funktion namens `multiply_and_add_5` zu erstellen, die zuerst ihre beiden Argumente multipliziert und dann 5 zum Ergebnis addiert. Wenn wir `multiply_and_add_5(5, 2)` aufrufen, erhalten wir das Ergebnis `15`.
