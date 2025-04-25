# カーネル

カーネルは、2 つのオブジェクト間の類似性の尺度です。機械学習のアルゴリズムの様々な場面で、特徴量間の非線形な関係を捉えるために使用されます。

Scikit-learn は、線形カーネル、多項式カーネル、シグモイドカーネル、RBF カーネル、ラプラシアンカーネル、およびチカ二乗カーネルなど、さまざまなカーネル関数を提供しています。

`pairwise_kernels` 関数を使って、2 つのサンプルセット間のペアワイズカーネルを計算してみましょう：

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

出力：

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
