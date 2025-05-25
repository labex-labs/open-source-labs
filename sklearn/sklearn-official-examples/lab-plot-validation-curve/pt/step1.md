# Carregando o Conjunto de Dados

Começaremos carregando o conjunto de dados de dígitos do scikit-learn e selecionando um subconjunto dos dados para classificação binária dos dígitos 1 e 2.

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # classificação binária: 1 vs 2
X, y = X[subset_mask], y[subset_mask]
```
