# Création du tracé

```python
fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].pcolormesh(Qx, Qz, Z, shading='gouraud')
axs[0].set_title('Sans valeurs masquées')
cmap = plt.colormaps[plt.rcParams['image.cmap']].with_extremes(bad='y')
axs[1].pcolormesh(Qx, Qz, Zm, shading='gouraud', cmap=cmap)
axs[1].set_title('Avec valeurs masquées')
axs[2].pcolormesh(Qx, Qz, Zm, shading='gouraud')
axs[2].set_title('Avec valeurs masquées')
fig.tight_layout()
plt.show()
```
