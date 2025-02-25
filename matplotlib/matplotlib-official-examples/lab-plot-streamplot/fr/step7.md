# Graphique de champ de flux avec masquage

Dans cette étape, nous allons créer un graphique de champ de flux avec masquage. Nous allons créer un masque et l'appliquer à la composante `U` de notre champ vectoriel. La région masquée sera ignorée par les lignes de courant.

```python
mask = np.zeros(U.shape, dtype=bool)
mask[40:60, 40:60] = True
U[:20, :20] = np.nan
U = np.ma.array(U, mask=mask)

plt.streamplot(X, Y, U, V, color='r')
plt.title('Streamplot with Masking')
plt.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5, cmap='gray', aspect='auto')
plt.gca().set_aspect('equal')
plt.show()
```
