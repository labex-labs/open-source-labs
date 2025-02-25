# Convertir un tableau de format large en format long

Maintenant, convertissons les données de NO2 au format large en format long en utilisant la fonction `melt`.

```python
# Réinitialiser l'index pour no2_pivoted
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Fusionner les données
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
