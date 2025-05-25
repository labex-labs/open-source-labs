# Preparação de Dados

Primeiro, criaremos um conjunto de dados grande com 80.000 amostras e o dividiremos em três conjuntos:

- Um conjunto para treinar os métodos de conjunto, que posteriormente serão usados como um transformador de engenharia de recursos.
- Um conjunto para treinar o modelo linear.
- Um conjunto para testar o modelo linear.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
