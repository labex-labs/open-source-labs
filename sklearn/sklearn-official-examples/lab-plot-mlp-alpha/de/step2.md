# Definiere Alphas

Wir werden verschiedene Werte für den Regularisierungsparameter alpha definieren. Wir werden np.logspace verwenden, um 5 logarithmisch gleichmäßig verteilte Werte zwischen 0,1 und 10 zu generieren.

```python
alphas = np.logspace(-1, 1, 5)
```
