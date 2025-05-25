# Gerar Dados Sintéticos

Usaremos a função `make_classification` do scikit-learn para gerar dados sintéticos. Esta função gera um problema de classificação aleatória de n classes, com n_informativas características informativas, n_redundantes características redundantes e n_clusters_per_class clusters por classe. Geraremos 1000 amostras com 2 características informativas e um estado aleatório de 1. Em seguida, dividiremos os dados em conjuntos de treino e teste com uma proporção de 60/40.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
