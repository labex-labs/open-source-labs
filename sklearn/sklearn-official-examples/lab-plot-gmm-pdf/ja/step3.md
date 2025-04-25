# ガウス混合モデルの適合

ここでは、scikit-learn の GaussianMixture クラスを使って GMM をデータセットに適合させます。コンポーネント数を 2 に設定し、共分散のタイプを「完全」に設定します。

```python
# 2 つのコンポーネントを持つガウス混合モデルを適合させる
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
