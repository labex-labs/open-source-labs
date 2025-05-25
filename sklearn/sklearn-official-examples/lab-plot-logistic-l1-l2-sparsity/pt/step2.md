# Carregar o Conjunto de Dados

Carregaremos o conjunto de dados de dígitos usando `datasets.load_digits(return_X_y=True)`. Também padronizaremos os dados usando `StandardScaler().fit_transform(X)`. A variável alvo será binária, onde 0-4 serão classificados como 0 e 5-9 como 1.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
