# Elegir un umbral para agrupar las características en clusters

Elegimos manualmente un umbral mediante la inspección visual del dendrograma para agrupar nuestras características en clusters y elegir una característica de cada cluster para mantener, seleccionar esas características de nuestro conjunto de datos y entrenar un nuevo bosque aleatorio. La precisión en la prueba del nuevo bosque aleatorio no cambió mucho en comparación con el bosque aleatorio entrenado en el conjunto de datos completo.

```python
cluster_ids = hierarchy.fcluster(dist_linkage, 1, criterion="distance")
cluster_id_to_feature_ids = defaultdict(list)
for idx, cluster_id in enumerate(cluster_ids):
    cluster_id_to_feature_ids[cluster_id].append(idx)
selected_features = [v[0] for v in cluster_id_to_feature_ids.values()]

X_train_sel = X_train[:, selected_features]
X_test_sel = X_test[:, selected_features]

clf_sel = RandomForestClassifier(n_estimators=100, random_state=42)
clf_sel.fit(X_train_sel, y_train)
print(
    "Precisión en los datos de prueba con características eliminadas: {:.2f}".format(
        clf_sel.score(X_test_sel, y_test)
    )
)
```
