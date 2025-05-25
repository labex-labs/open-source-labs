# Dividir o conjunto de dados em conjuntos de treino e teste

Em seguida, dividiremos o conjunto de dados em conjuntos de treino e teste usando a função `train_test_split` do scikit-learn. Usaremos 90% dos dados para treino e 10% para teste.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
