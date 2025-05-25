# Importar Bibliotecas e Gerar Conjunto de Dados

Começamos importando as bibliotecas necessárias e gerando um conjunto de dados sintético de classificação binária com 100.000 amostras e 20 características. Das 20 características, apenas 2 são informativas, 2 são redundantes e as restantes 16 são não informativas. Das 100.000 amostras, 100 serão usadas para ajustar os modelos e as restantes para testes.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Gerar conjunto de dados
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Amostras usadas para treinar os modelos
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```
