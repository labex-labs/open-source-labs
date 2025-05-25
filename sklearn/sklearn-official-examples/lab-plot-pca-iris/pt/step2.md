# Carregar o conjunto de dados

Em seguida, carregaremos o conjunto de dados Iris usando a função `load_iris()` do scikit-learn. Separaremos então as variáveis de características (X) e alvo (y).

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
