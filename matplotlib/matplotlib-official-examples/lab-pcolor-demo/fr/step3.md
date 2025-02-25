# Pcolor avec une échelle logarithmique

La troisième étape est de créer un graphique Pcolor avec une échelle logarithmique. Cela est utile lorsque vous avez des données avec une large plage de valeurs.

```python
N = 100
X, Y = np.meshgrid(np.linspace(-3, 3, N), np.linspace(-2, 2, N))

# Une bosse basse avec une pointe sortante.
# Nécessite d'avoir l'axe z/couleur sur une échelle logarithmique, afin que nous voyions à la fois la bosse et la pointe.
# Une échelle linéaire ne montre que la pointe.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(X, Y, Z, shading='auto',
               norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap='PuBu_r')
fig.colorbar(c, ax=ax0)

c = ax1.pcolor(X, Y, Z, cmap='PuBu_r', shading='auto')
fig.colorbar(c, ax=ax1)

plt.show()
```
