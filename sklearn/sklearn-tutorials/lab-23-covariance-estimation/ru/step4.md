# Разреженная обратная ковариация

Оценка разреженной обратной ковариации, также известная как подбор ковариации, имеет целью оценить разреженную матрицу точности, где обратная матрица ковариации представляет собой матрицу частичных корреляций. В пакете `sklearn.covariance` есть класс `GraphicalLasso` для оценки разреженной обратной ковариационной матрицы с использованием штрафа l1.

```python
from sklearn.covariance import GraphicalLasso

# Create a GraphicalLasso object and fit it to the data
graphical_lasso = GraphicalLasso().fit(data)

# Compute the sparse inverse covariance matrix
sparse_inverse_covariance_matrix = graphical_lasso.precision_
```
