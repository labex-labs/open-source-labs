# Créez le graphique à barre d'erreur avec les limites supérieure et inférieure

Dans cette étape, nous créons un graphique à barre d'erreur avec les limites supérieure et inférieure.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
