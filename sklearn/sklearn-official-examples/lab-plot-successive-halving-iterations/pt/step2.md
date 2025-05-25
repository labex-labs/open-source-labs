# Carregando o Conjunto de Dados

A função `make_classification` do módulo `sklearn.datasets` é utilizada para gerar um conjunto de dados de classificação. O conjunto de dados contém 400 amostras com 12 características. O código para carregar o conjunto de dados é o seguinte:

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
