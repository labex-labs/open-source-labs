# Sélectionner les caractéristiques et définir la carte des caractéristiques

Ensuite, nous sélectionnons deux caractéristiques de l'ensemble de données pour faciliter la visualisation et définissons une carte des noms des caractéristiques pour une meilleure visualisation.

```python
# Sélectionner deux caractéristiques
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Définir la carte des caractéristiques
feature_mapping = {
    "MedInc": "Revenu médian dans le bloc",
    "AveOccup": "Occupation moyenne des maisons",
}
```
