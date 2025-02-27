# Выбрать порог для группировки признаков в кластеры

Мы вручную выбираем порог путём визуального осмотра дендрограммы, чтобы сгруппировать наши признаки в кластеры и выбрать из каждого кластера один признак для сохранения, выбрать эти признаки из нашего набора данных и обучить новый случайный лес. Точность теста нового случайного леса не изменилась существенно по сравнению с случайным лесом, обученным на полном наборе данных.

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
