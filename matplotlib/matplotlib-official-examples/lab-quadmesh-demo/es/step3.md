# Creando el gráfico

```python
fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].pcolormesh(Qx, Qz, Z, shading='gouraud')
axs[0].set_title('Sin valores enmascarados')
cmap = plt.colormaps[plt.rcParams['image.cmap']].with_extremes(bad='y')
axs[1].pcolormesh(Qx, Qz, Zm, shading='gouraud', cmap=cmap)
axs[1].set_title('Con valores enmascarados')
axs[2].pcolormesh(Qx, Qz, Zm, shading='gouraud')
axs[2].set_title('Con valores enmascarados')
fig.tight_layout()
plt.show()
```
