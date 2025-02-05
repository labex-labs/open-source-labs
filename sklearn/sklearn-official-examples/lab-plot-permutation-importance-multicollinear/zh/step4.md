# 选择一个阈值将特征分组为聚类

我们通过直观检查树形图来手动选择一个阈值，以便将特征分组为聚类，并从每个聚类中选择一个特征保留下来，从数据集中选择这些特征，然后训练一个新的随机森林。与在完整数据集上训练的随机森林相比，新随机森林的测试准确率变化不大。

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
