# ディリクレ過程事前分布を持つベイジアンガウス混合モデルのフィッティング

次に、ディリクレ過程事前分布を持つベイジアンガウス混合モデルをフィッティングします。データの微細な構造をモデル化するために、モデルにより多くの自由度を与えるために、事前分布の濃度を高い値に設定します。

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="kmeans",
    max_iter=100,
    random_state=2,
).fit(X)
```
