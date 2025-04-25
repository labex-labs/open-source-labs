# サポートベクターマシン（SVM）分類モデルの訓練

```python
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}

clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
```

変換後のデータを使用して SVM 分類モデルを訓練します。`RandomizedSearchCV()`を使用して、SVM モデルの最適なハイパーパラメータを見つけます。
