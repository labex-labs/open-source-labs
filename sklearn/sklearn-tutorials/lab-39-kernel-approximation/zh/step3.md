# 加性卡方（ACS）核近似

ACS 核是一种用于直方图的核，常用于计算机视觉。AdditiveChi2Sampler 类为这个核提供了一种近似映射。

要使用 AdditiveChi2Sampler 进行核近似，请遵循以下步骤：

1. 使用所需的样本数量（n）和正则化参数（c）初始化 AdditiveChi2Sampler 对象。

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. 将 AdditiveChi2Sampler 对象拟合到你的训练数据。

```python
additive_chi2_sampler.fit(X_train)
```

3. 使用 AdditiveChi2Sampler 对象变换你的训练数据和测试数据。

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
