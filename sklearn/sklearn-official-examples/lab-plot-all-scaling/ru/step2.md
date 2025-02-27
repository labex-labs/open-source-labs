# Выбор признаков и определение отображения признаков

Далее мы выбираем два признака из датасета, чтобы сделать визуализацию проще, и определяем отображение имен признаков для более наглядной визуализации.

```python
# Select two features
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Define feature mapping
feature_mapping = {
    "MedInc": "Median income in block",
    "AveOccup": "Average house occupancy",
}
```
