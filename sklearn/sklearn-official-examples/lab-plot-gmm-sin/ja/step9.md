# 高濃度事前分布を持つベイジアン GMM の結果をプロットする

ディリクレ過程事前分布と高い濃度事前分布を持つベイジアンガウス混合モデルの結果をプロットします。

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    2,
    "Bayesian Gaussian mixture models with a Dirichlet process prior "
    r"for $\gamma_0=100$",
)
```
