# Configurez la trame initiale

Ensuite, nous allons configurer la trame initiale. Nous allons créer une onde sinusoïdale avec une fréquence de 2 Hz à l'aide de la fonction `arange` de `numpy`, et la tracer à l'aide de la fonction `plot` de `matplotlib.pyplot`.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
