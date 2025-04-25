# EM を用いたガウス混合モデルのフィッティング

期待最大化アルゴリズムを用いて 10 個のコンポーネントで古典的なガウス混合モデルをフィッティングします。

```python
# Fit a Gaussian mixture with EM using ten components
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
