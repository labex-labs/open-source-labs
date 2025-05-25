# Conjunto de Dados

Utilizaremos um conjunto de dados sintético para classificação binária com 100.000 amostras e 20 características. Das 20 características, apenas 2 são informativas, 10 são redundantes (combinações aleatórias das características informativas) e as restantes 8 são não informativas (números aleatórios). Das 100.000 amostras, 1.000 serão utilizadas para o ajuste do modelo e o restante para testes.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
