# 数据准备

首先，我们将创建一个包含80,000个样本的大型数据集，并将其分为三组：

- 一组用于训练集成方法，这些方法稍后将用作特征工程变换器
- 一组用于训练线性模型
- 一组用于测试线性模型。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
