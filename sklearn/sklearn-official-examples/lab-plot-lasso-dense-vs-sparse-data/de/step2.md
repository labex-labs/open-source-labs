# Dichte Daten generieren

Als nächstes generieren wir einige dichte Daten, die wir für die Lasso-Regression verwenden werden. Wir verwenden die `make_regression`-Funktion von Scikit-learn, um 200 Proben mit 5000 Merkmalen zu generieren.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
