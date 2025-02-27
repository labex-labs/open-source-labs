# ディリクレ過程事前分布を持つベイジアンガウス混合モデルのフィッティング

次に、ディリクレ過程事前分布を持つベイジアンガウス混合モデルをフィッティングします。活性なコンポーネントの数が少ないことをモデルが好むように、事前分布の濃度を低い値に設定します。

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e-2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="random",
    max_iter=100,
    random_state=2,
).fit(X)
```
