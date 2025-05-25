# Importação de bibliotecas e geração de dados

O primeiro passo é importar as bibliotecas necessárias e gerar os dados. Usaremos o numpy e o matplotlib para gerar e visualizar os dados, e o scikit-learn para construir o modelo SVM de uma classe.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Gerar dados de treinamento
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Gerar algumas observações regulares e novas
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Gerar algumas observações novas e anormais
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```

# Ajustar o modelo SVM de uma classe

Em seguida, ajustaremos o modelo SVM de uma classe aos dados gerados.

```python
# Ajustar o modelo
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Prever as etiquetas para os dados de treinamento, observações regulares e novas, e observações novas anormais
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
