# Conjunto de Dados e Modelo

Usaremos o conjunto de dados iris e um classificador Linear SVC para diferenciar dois tipos de íris. Primeiro, importamos as bibliotecas necessárias e carregamos o conjunto de dados.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

Em seguida, adicionaremos características ruidosas ao conjunto de dados e dividiremos em conjuntos de treino e teste.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

Finalmente, escalaremos os dados usando um `StandardScaler` e ajustaremos um classificador `Linear SVC` aos dados de treino.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
