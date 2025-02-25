# Daten erstellen

In diesem Schritt erstellen wir die Daten, die wir verwenden werden, um unseren Fehlerbalkendiagramm zu erstellen.

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```
