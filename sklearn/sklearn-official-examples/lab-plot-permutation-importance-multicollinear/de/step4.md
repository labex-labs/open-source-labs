# Einen Schwellenwert auswählen, um Features in Cluster zu gruppieren

Wir wählen manuell einen Schwellenwert aus, indem wir das Dendrogramm visuell untersuchen, um unsere Features in Cluster zu gruppieren und aus jedem Cluster ein Feature auszuwählen, um zu behalten. Wir wählen diese Features aus unserem Datensatz und trainieren einen neuen Random Forest. Die Testgenauigkeit des neuen Random Forests hat im Vergleich zum auf dem vollständigen Datensatz trainierten Random Forest nicht viel geändert.

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
