# ガウス混合モデルをフィットさせる

ここで、`sklearn.mixture` モジュールの `GaussianMixture` クラスを使って、ガウス混合モデルをデータにフィットさせることができます。希望するコンポーネント数とその他使用したいパラメータを指定します。

```python
# Fit a Gaussian Mixture Model
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
