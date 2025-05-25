# Carregar os Dados

Em seguida, carregamos o conjunto de dados iris do Scikit-learn e selecionamos apenas as duas primeiras características para fins de visualização.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
