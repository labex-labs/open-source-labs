# Mittelwert und Standardabweichung berechnen

Als nächstes berechnen wir den Mittelwert und die Standardabweichung von jedem der 100 Datensätze. Wir verwenden die mean- und std-Funktionen von numpy, um diese Werte zu berechnen.

```python
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
