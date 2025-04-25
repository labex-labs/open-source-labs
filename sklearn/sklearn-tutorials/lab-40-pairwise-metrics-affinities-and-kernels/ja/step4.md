# 多項式カーネル

多項式カーネルは、2 つのベクトルの次元間の相互作用を考慮して、それらの類似度を計算します。

Scikit-learn は、ベクトル間の多項式カーネルを計算する `polynomial_kernel` 関数を提供しています。

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

出力：

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
