# 用于核近似的 Nystroem 方法

Nystroem 方法是一种使用低秩近似来近似核的通用技术。它对评估核的数据集进行子采样。默认情况下，它使用 RBF 核，但也可以与任何核函数或预先计算的核矩阵一起使用。

要使用 Nystroem 方法进行核近似，请遵循以下步骤：

1. 使用所需的组件数量（即特征变换的目标维度）初始化 Nystroem 对象。

```python
from sklearn.kernel_approximation import Nystroem

n_components = 100
nystroem = Nystroem(n_components=n_components)
```

2. 将 Nystroem 对象拟合到你的训练数据。

```python
nystroem.fit(X_train)
```

3. 使用 Nystroem 对象变换你的训练数据和测试数据。

```python
X_train_transformed = nystroem.transform(X_train)
X_test_transformed = nystroem.transform(X_test)
```
