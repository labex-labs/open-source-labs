# Convertir un tableau de format long en format large

Nous allons maintenant convertir les données de qualité de l'air au format long en format large en utilisant la fonction `pivot`.

```python
# Filtrer pour ne conserver que les données de no2
no2 = air_quality[air_quality["parameter"] == "no2"]

# Utiliser 2 mesures (head) pour chaque emplacement (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# Transformer les données en tableau pivoté
no2_subset.pivot(columns="location", values="value")
```
