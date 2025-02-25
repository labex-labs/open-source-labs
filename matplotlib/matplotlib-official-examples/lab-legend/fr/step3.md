# Création du graphique

Maintenant, nous sommes prêts à créer notre graphique. Nous allons utiliser la fonction `plot` de Matplotlib pour tracer trois lignes sur le même graphique, chacune avec une étiquette prédéfinie. Nous utiliserons le paramètre `label` pour attribuer les étiquettes à chaque ligne.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
