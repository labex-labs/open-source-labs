# Seleccionar características y definir el mapeo de características

A continuación, seleccionamos dos características del conjunto de datos para facilitar la visualización y definimos un mapeo de los nombres de las características para una mejor visualización.

```python
# Seleccionar dos características
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Definir el mapeo de características
feature_mapping = {
    "MedInc": "Median income in block",
    "AveOccup": "Average house occupancy",
}
```
