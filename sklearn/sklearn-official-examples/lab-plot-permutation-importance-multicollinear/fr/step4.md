# Choisir un seuil pour regrouper les fonctionnalités en clusters

Nous choisissons manuellement un seuil en examinant visuellement le dendrogramme pour regrouper nos fonctionnalités en clusters et choisir une fonctionnalité de chaque cluster à conserver, sélectionner ces fonctionnalités dans notre ensemble de données et entraîner un nouveau forêt aléatoire. La précision sur le test du nouveau forêt aléatoire n'a pas beaucoup changé par rapport à la forêt aléatoire entraînée sur l'ensemble de données complet.

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
    "Accuracy on test data with features removed: {:.2f}".format(
        clf_sel.score(X_test_sel, y_test)
    )
)
```
