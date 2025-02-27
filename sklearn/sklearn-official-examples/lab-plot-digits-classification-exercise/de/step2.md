# Vorverarbeiten der Daten

Anschließend werden wir die Daten vorverarbeiten, indem wir die Merkmale auf einen Wertebereich von [0, 1] skalieren, indem wir den Maximalwert der Daten verwenden. Dies kann durch Teilen der Eingabedaten durch den Maximalwert der Eingabedaten erreicht werden.

```python
X_digits = X_digits / X_digits.max()
```
