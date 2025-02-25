# Créez le graphique à barre d'erreur avec les deux limites (valeur par défaut)

Dans cette étape, nous créons un graphique à barre d'erreur avec des limites supérieure et inférieure, ce qui est le comportement par défaut.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
