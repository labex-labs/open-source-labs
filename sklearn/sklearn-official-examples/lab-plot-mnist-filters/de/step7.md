# Gewichte visualisieren

Schließlich visualisieren wir die Gewichte der ersten Schicht des MLP. Wir erstellen ein 4x4-Raster von Teilplots und zeigen jedes Gewicht als 28x28 Pixel Graustufenbild an.

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
