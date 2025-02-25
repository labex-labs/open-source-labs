# Ajout d'une ligne pour délimiter les régions masquées

Enfin, nous ajoutons une ligne pour délimiter les régions masquées. Nous créons un tableau de valeurs de theta et traçons un cercle de rayon `r0` en utilisant `np.cos(theta)` et `np.sin(theta)`.

```python
# Affiche la limite entre les régions :
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
