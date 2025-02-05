# 加载数据集并分割数据

首先，我们将使用 Scikit-Learn 库加载数字数据集。这个数据集由 0 到 9 的数字的 8x8 图像组成。每个图像都表示为一个 64 个特征的数组。我们将把数据分割为特征和目标变量。

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```
