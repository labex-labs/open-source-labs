# Carregar o Conjunto de Dados Iris

Carregaremos o Conjunto de Dados Iris usando a função `load_iris` embutida do Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # apenas as duas primeiras características são selecionadas.
y = iris.target
```
