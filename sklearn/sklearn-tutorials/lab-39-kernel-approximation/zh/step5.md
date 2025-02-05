# 通过张量草图进行多项式核近似

多项式核是一种常用的核函数，用于对特征之间的交互进行建模。PolynomialCountSketch 类提供了一种使用张量草图方法来近似此核的可扩展方法。

要使用 PolynomialCountSketch 进行核近似，请遵循以下步骤：

1. 使用所需的次数（d）和组件数量初始化 PolynomialCountSketch 对象。

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. 将 PolynomialCountSketch 对象拟合到你的训练数据。

```python
polynomial_count_sketch.fit(X_train)
```

3. 使用 PolynomialCountSketch 对象变换你的训练数据和测试数据。

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
