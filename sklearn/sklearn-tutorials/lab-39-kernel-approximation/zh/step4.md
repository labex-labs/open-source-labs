# 偏斜卡方（SCS）核近似

SCS 核是指数化卡方核的一种变体，它允许对特征映射进行简单的蒙特卡罗近似。SkewedChi2Sampler 类为这个核提供了一种近似映射。

要使用 SkewedChi2Sampler 进行核近似，请遵循以下步骤：

1. 使用所需的样本数量（n）和正则化参数（c）初始化 SkewedChi2Sampler 对象。

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. 将 SkewedChi2Sampler 对象拟合到你的训练数据。

```python
skewed_chi2_sampler.fit(X_train)
```

3. 使用 SkewedChi2Sampler 对象变换你的训练数据和测试数据。

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
