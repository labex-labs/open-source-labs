# Ajoutez une ligne de meilleure ajustement

Dans cette étape, nous allons ajouter une ligne de meilleure ajustement à l'histogramme. Nous allons calculer les valeurs y pour la ligne et la tracer au-dessus de l'histogramme.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
