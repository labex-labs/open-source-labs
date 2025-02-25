# Daten generieren

Als nächstes werden wir einige zufällige 2D-Daten generieren, die wir für das Histogramm verwenden. Wir werden die `random.rand()`-Funktion von NumPy verwenden, um 100 zufällige Werte für beide Variablen x und y zu generieren.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
