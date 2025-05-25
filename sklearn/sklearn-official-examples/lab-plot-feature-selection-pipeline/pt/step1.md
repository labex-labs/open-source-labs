# Gerar e Dividir o Conjunto de Dados

Começaremos gerando um conjunto de dados de classificação binária usando a função `make_classification` do Scikit-learn. Também dividiremos o conjunto de dados em subconjuntos de treinamento e teste usando a função `train_test_split` do Scikit-learn.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```
