# Kleinstes gemeinsames Vielfache - Herausforderung

## Problemstellung

Schreiben Sie eine Funktion `lcm(numbers)`, die eine Liste von Zahlen als Argument erhält und ihr kleinstes gemeinsames Vielfache zurückgibt. Ihre Funktion sollte die folgende Formel verwenden, um das KGV von zwei Zahlen `x` und `y` zu berechnen: `kgv(x, y) = x * y / ggT(x, y)`, wobei `ggT(x, y)` der größte gemeinsame Teiler von `x` und `y` ist.

Um dieses Problem zu lösen, können Sie die Funktion `functools.reduce()` verwenden, um die `kgv()`-Formel auf alle Zahlen in der Liste anzuwenden. Sie können auch die Funktion `math.gcd()` verwenden, um den größten gemeinsamen Teiler von zwei Zahlen zu berechnen.

## Beispiel

```python
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```
