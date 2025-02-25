# Créer la figure et les axes

Dans cette étape, vous allez créer la figure et les axes pour le tracé. Vous ajusterez également la position des axes pour laisser de la place aux curseurs.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```
