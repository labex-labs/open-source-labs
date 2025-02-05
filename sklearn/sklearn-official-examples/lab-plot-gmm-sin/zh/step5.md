# 使用狄利克雷过程先验拟合贝叶斯高斯混合模型

现在我们将使用狄利克雷过程先验来拟合一个贝叶斯高斯混合模型。我们将设置一个较低的浓度先验值，以使模型倾向于较少数量的活跃分量。

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
