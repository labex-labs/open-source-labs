# Daten erstellen

In diesem Schritt werden wir die Daten für unser Fehlerbalkendiagramm erstellen. Wir werden NumPy verwenden, um ein Array von Theta-Werten und ein Array von entsprechenden Radius-Werten zu erstellen.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
