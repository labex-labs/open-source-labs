# Gerar Conjunto de Dados Sintético

Geramos um conjunto de dados sintético onde `X` e `y` estão linearmente relacionados. Dez dos recursos de `X` serão usados para gerar `y`. Os outros recursos não são úteis na previsão de `y`. Além disso, geramos um conjunto de dados onde `n_samples == n_features`. Tal cenário é desafiador para um modelo OLS e pode levar a pesos arbitrariamente grandes. Ter uma prioridade nos pesos e uma penalidade alivia o problema. Finalmente, é adicionado ruído gaussiano.

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
