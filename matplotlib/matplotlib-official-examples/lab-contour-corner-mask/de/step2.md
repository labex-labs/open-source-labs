# Erstellen von Daten zum Plotten

In diesem Schritt werden wir Daten erstellen, die auf einem Konturplot geplottet werden sollen. Wir verwenden die Funktion `np.meshgrid()`, um ein Gitter von Punkten zu erstellen, und berechnen dann die `z`-Werte mit Hilfe der Sinus- und Kosinusfunktionen.

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
