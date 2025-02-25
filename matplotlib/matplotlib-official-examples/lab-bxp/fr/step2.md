# Calcul des statistiques du diagramme en boîte

La fonction `boxplot_stats()` du module `matplotlib.cbook` calcule les statistiques nécessaires pour le diagramme en boîte. Nous passons les données et les étiquettes en tant que paramètres.

```python
# Calcul des statistiques du diagramme en boîte
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
