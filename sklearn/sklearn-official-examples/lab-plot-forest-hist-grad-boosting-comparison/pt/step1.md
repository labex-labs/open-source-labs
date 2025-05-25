# Carregar Conjunto de Dados

Vamos carregar o conjunto de dados de habitação da Califórnia usando a função `fetch_california_housing` do scikit-learn. Este conjunto de dados consiste em 20.640 amostras e 8 características.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"O conjunto de dados consiste em {n_samples} amostras e {n_features} características")
```
