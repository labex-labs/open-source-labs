# Generieren von zufälligen Daten

Wir werden zufällige Daten mit der `make_regression`-Funktion aus scikit-learn generieren. Wir werden `n_samples` auf 10, `n_features` auf 10 und `random_state` auf 1 setzen. Diese Funktion wird unsere Eingabefeatures X, unsere Zielfunktion y und die wahren Koeffizientenwerte w zurückgeben.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
