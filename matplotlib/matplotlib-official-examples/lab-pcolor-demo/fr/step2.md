# Comparaison de Pcolor avec des fonctions similaires

La deuxième étape est de comparer Pcolor avec des fonctions similaires, telles que Pcolormesh, Imshow et Pcolorfast. Cela vous aidera à comprendre les différences entre ces fonctions et quand utiliser chacune d'entre elles.

```python
# rendant ces valeurs plus petites pour augmenter la résolution
dx, dy = 0.15, 0.05

# générer 2 grilles 2D pour les bornes x et y
y, x = np.mgrid[-3:3+dy:dy, -3:3+dx:dx]
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# x et y sont des bornes, donc z devrait être la valeur *à l'intérieur* de ces bornes.
# Par conséquent, supprimer la dernière valeur du tableau z.
z = z[:-1, :-1]
z_min, z_max = -abs(z).max(), abs(z).max()

fig, axs = plt.subplots(2, 2)

ax = axs[0, 0]
c = ax.pcolor(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolor')
fig.colorbar(c, ax=ax)

ax = axs[0, 1]
c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolormesh')
fig.colorbar(c, ax=ax)

ax = axs[1, 0]
c = ax.imshow(z, cmap='RdBu', vmin=z_min, vmax=z_max,
              extent=[x.min(), x.max(), y.min(), y.max()],
              interpolation='proche', origine='inférieure', aspect='auto')
ax.set_title('image (proche, aspect="auto")')
fig.colorbar(c, ax=ax)

ax = axs[1, 1]
c = ax.pcolorfast(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolorfast')
fig.colorbar(c, ax=ax)

fig.tight_layout()
plt.show()
```
