# Erstellen des Diagramms

```python
fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].pcolormesh(Qx, Qz, Z, shading='gouraud')
axs[0].set_title('Ohne maskierte Werte')
cmap = plt.colormaps[plt.rcParams['image.cmap']].with_extremes(bad='y')
axs[1].pcolormesh(Qx, Qz, Zm, shading='gouraud', cmap=cmap)
axs[1].set_title('Mit maskierten Werten')
axs[2].pcolormesh(Qx, Qz, Zm, shading='gouraud')
axs[2].set_title('Mit maskierten Werten')
fig.tight_layout()
plt.show()
```
