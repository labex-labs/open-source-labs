# Tracez un autre exemple

Nous allons maintenant tracer un autre exemple de conversion du nombre d'ondes en longueur d'onde dans une échelle log-log. Nous utiliserons un spectre aléatoire pour cet exemple.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
