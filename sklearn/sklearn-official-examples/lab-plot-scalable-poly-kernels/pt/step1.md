# Carregar e Preparar os Dados

Primeiro, carregaremos o conjunto de dados Covtype e o transformaremos num problema de classificação binária, selecionando apenas uma classe. Em seguida, dividiremos os dados em conjuntos de treino e teste e normalizaremos as características.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer
from sklearn.pipeline import make_pipeline

# Carregar o conjunto de dados Covtype, selecionando apenas uma classe
X, y = fetch_covtype(return_X_y=True)
y[y != 2] = 0
y[y == 2] = 1

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# Normalizar as características
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
