# Créer des sous-graphiques pour chaque colonne

Nous pouvons créer des sous-graphiques distincts pour chaque colonne de données en utilisant l'argument `subplots`.

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
