# Setze die Anfangsdiagramm ein

Als nächstes legen wir das Anfangsdiagramm fest. Wir werden eine Sinuswelle mit einer Frequenz von 2 Hz mithilfe der `arange`-Funktion von `numpy` erstellen und sie mit der `plot`-Funktion von `matplotlib.pyplot` darstellen.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
