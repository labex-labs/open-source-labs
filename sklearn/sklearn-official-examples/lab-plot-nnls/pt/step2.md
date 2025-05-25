# Dividir os Dados em Conjuntos de Treino e Teste

Dividiremos os nossos dados em um conjunto de treino e um conjunto de teste, com 50% dos dados em cada conjunto.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
