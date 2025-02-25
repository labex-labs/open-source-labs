# Créez le graphique à barre d'erreur avec seulement les limites supérieures

Dans cette étape, nous créons un graphique à barre d'erreur avec seulement les limites supérieures.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
