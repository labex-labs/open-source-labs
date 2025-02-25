# Erstellen von Daten für den Linienplot

In diesem Schritt werden wir Daten für unseren Linienplot erstellen. Wir werden die `linspace`-Funktion von NumPy verwenden, um ein Array von gleichmäßig verteilten Werten zwischen 0 und 10 zu erstellen. Wir werden auch einige zufälliges Rauschen mit der `random.randn`-Funktion von NumPy generieren.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
