# 使用狄利克雷过程先验拟合贝叶斯高斯混合模型

现在我们将使用狄利克雷过程先验来拟合一个贝叶斯高斯混合模型。我们将设置一个较高的浓度先验值，以便让模型有更多自由度来对数据的细粒度结构进行建模。

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
