# Carregar o conjunto de dados

Em seguida, carregamos o conjunto de dados iris do Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # apenas as duas primeiras características são usadas para visualização
y = iris.target
n_features = X.shape[1]
```
