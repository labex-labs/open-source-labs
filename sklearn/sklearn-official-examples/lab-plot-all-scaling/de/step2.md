# Merkmale auswählen und Merkmalszuordnung definieren

Als nächstes wählen wir zwei Merkmale aus dem Datensatz, um die Visualisierung zu erleichtern, und definieren eine Zuordnung der Merkmalsnamen für eine bessere Visualisierung.

```python
# Wähle zwei Merkmale
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Definiere Merkmalszuordnung
feature_mapping = {
    "MedInc": "Median income in block",
    "AveOccup": "Average house occupancy",
}
```
