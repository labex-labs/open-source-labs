# 主成分分析（PCA）の実行

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

主成分分析（Principal Component Analysis, PCA）を実行して、入力データから特徴量を抽出します。成分数を150に設定し、PCAモデルを訓練データに適合させます。次に、固有顔（eigenfaces）を取得し、入力データを主成分に変換します。
