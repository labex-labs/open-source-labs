# 高濃度事前分布を持つベイジアン GMM からサンプリングする

次に、ディリクレ過程事前分布と高い濃度事前分布を持つベイジアンガウス混合モデルからサンプリングします。

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    1,
    "Gaussian mixture with a Dirichlet process prior "
    r"for $\gamma_0=100$ sampled with $2000$ samples.",
)
```
