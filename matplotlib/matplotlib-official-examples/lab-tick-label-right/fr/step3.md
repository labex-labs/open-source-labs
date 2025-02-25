# Créez un graphique d'exemple

Créeons un graphique d'exemple pour voir à quoi cela ressemble avec les étiquettes d'échelonnement de l'axe des y sur le côté droit.

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
