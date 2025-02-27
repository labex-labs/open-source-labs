# Visualisierung der Ergebnisse

Schließlich lassen Sie uns die Ergebnisse unseres isotonen Regressionsmodells visualisieren. Wir können die ursprünglichen Datenpunkte als Streudiagrammpunkte und die vorhergesagten Werte als Linie plotten.

```python
import matplotlib.pyplot as plt

# Plot the original data and predicted values
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
