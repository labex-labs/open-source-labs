# Classificação por Processo Gaussiano (GPC)

A classe `GaussianProcessClassifier` implementa GPC para classificação probabilística. Ela coloca uma prior de GP em uma função latente, que é então comprimida por meio de uma função de ligação para obter as probabilidades de classe. O GPC suporta classificação multiclasse realizando treinamento e previsão baseados em um contra todos ou um contra um.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier

# Cria um modelo GPC com um kernel RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajusta o modelo aos dados de treino
model.fit(X_train, y_train)

# Prediz usando o modelo treinado
y_pred = model.predict(X_test)
```
