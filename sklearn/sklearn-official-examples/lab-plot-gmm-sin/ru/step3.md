# Подгонка смеси Гауссовых распределений с использованием EM

Мы подгоним классическую смесь Гауссовых распределений с 10 компонентами с использованием алгоритма Expectation-Maximization.

```python
# Fit a Gaussian mixture with EM using ten components
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
