# Créer le graphique

Maintenant, nous allons créer le graphique en utilisant `matplotlib`. Nous allons tracer les trois ondes sinusoïdales sur le même graphique et définir la visibilité de la première onde sur `False` car nous voulons commencer avec elle cachée.

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```
