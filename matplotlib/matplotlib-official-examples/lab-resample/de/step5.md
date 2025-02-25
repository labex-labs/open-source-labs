# Erstellen des Signals

Wir werden ein Signal mit NumPy erstellen. Wir werden ein Array xdata mit der linspace-Funktion erstellen, wobei start=16, stop=365 und num=(365-16)\*4. Wir werden ein Array ydata mit den sin- und cos-Funktionen erstellen.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
