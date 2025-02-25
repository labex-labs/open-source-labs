# Créez le graphique à barre d'erreur avec des sous - ensembles de limites supérieure et inférieure

Dans cette étape, nous créons un graphique à barre d'erreur avec des sous - ensembles de limites supérieure et inférieure.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
