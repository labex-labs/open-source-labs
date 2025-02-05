# 核函数

核函数是衡量两个对象之间相似度的指标。它们可用于各种机器学习算法中，以捕捉特征之间的非线性关系。

Scikit-learn 提供了不同的核函数，如线性核、多项式核、sigmoid 核、径向基函数（RBF）核、拉普拉斯核和卡方核。

让我们使用 `pairwise_kernels` 函数计算两组样本之间的成对核函数：

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# 使用线性核计算 X 和 Y 之间的成对核函数
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

输出：

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
