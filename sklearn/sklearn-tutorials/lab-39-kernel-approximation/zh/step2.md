# 径向基函数（RBF）核近似

RBFSampler 类实现了 RBF 核的近似映射，也称为随机厨房水槽（Random Kitchen Sinks）。这种技术使我们能够在应用线性算法（如线性支持向量机或逻辑回归）之前，显式地对核映射进行建模。

要使用 RBFSampler 进行核近似，请遵循以下步骤：

1. 使用所需的 gamma 值（RBF 核的参数）和组件数量初始化 RBFSampler 对象。

```python
from sklearn.kernel_approximation import RBFSampler

gamma = 0.1
n_components = 100
rbf_sampler = RBFSampler(gamma=gamma, n_components=n_components)
```

2. 将 RBFSampler 对象拟合到你的训练数据。

```python
rbf_sampler.fit(X_train)
```

3. 使用 RBFSampler 对象变换你的训练数据和测试数据。

```python
X_train_transformed = rbf_sampler.transform(X_train)
X_test_transformed = rbf_sampler.transform(X_test)
```
