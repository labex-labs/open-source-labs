# 多项式核函数

多项式核函数通过考虑两个向量维度之间的相互作用来计算它们之间的相似度。

Scikit-learn 提供了 `polynomial_kernel` 函数来计算向量之间的多项式核函数。

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# 计算 X 和 Y 之间的多项式核函数
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

输出：

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
