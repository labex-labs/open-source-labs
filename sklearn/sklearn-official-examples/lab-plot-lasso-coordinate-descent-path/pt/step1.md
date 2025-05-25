# Carregar o Conjunto de Dados

Neste passo, carregaremos o conjunto de dados de diabetes da biblioteca scikit-learn e padronizaremos os dados.

```python
from sklearn import datasets

# Carregar o conjunto de dados de diabetes
X, y = datasets.load_diabetes(return_X_y=True)

# Padronizar os dados
X /= X.std(axis=0)
```
