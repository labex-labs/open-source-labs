# Daten generieren

In diesem Schritt generieren wir einige Daten, die wir für das Diagramm verwenden werden. Wir werden eine Gaußsche gefärbte Störung mit der `convolve`-Funktion von NumPy erstellen und sie mit Matplotlib darstellen.

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```
