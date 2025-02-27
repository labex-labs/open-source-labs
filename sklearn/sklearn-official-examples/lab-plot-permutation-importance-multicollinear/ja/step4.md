# クラスタに特徴量をグループ化するための閾値を選ぶ

デンドログラムを目視で確認することで、手動で閾値を選び、特徴量をクラスタにグループ化し、各クラスタから1つの特徴量を選んで残します。そして、データセットからそれらの特徴量を選択し、新しいランダムフォレストを学習します。完全なデータセットで学習したランダムフォレストと比較すると、新しいランダムフォレストのテスト精度はあまり変化しませんでした。

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
