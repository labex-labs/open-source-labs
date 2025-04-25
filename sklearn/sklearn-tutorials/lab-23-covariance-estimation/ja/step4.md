# 疎な逆共分散

疎な逆共分散推定は、共分散選択とも呼ばれ、共分散行列の行列逆行列が部分相関行列を表す疎な精度行列を推定することを目的としています。`sklearn.covariance`パッケージには、l1 ペナルティを使用して疎な逆共分散行列を推定するための`GraphicalLasso`クラスが含まれています。

```python
from sklearn.covariance import GraphicalLasso

# Create a GraphicalLasso object and fit it to the data
graphical_lasso = GraphicalLasso().fit(data)

# Compute the sparse inverse covariance matrix
sparse_inverse_covariance_matrix = graphical_lasso.precision_
```
