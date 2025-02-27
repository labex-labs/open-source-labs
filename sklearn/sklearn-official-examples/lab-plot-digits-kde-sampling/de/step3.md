# Neue Samples generieren

Wir verwenden den besten Schätzer, um 44 neue Punkte aus den Daten zu entnehmen. Anschließend transformieren wir die neuen Daten zurück in ihre ursprüngliche 64-Dimension mit der Inverse der PCA.

```python
# entnehmen Sie 44 neue Punkte aus den Daten
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
