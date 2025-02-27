# Definiere die Hyperparameterwerte zum Testen

Wir werden verschiedene Werte des Regularisierungsparameters C testen, der das Kompromissverhältnis zwischen der Maximalisierung der Margin und der Minimierung der Klassifizierungsfehler steuert. Wir werden 10 logarithmisch gleichmäßig verteilte Werte zwischen 10^-10 und 1 testen.

```python
C_s = np.logspace(-10, 0, 10)
```
