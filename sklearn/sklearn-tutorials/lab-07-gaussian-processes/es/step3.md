# Clasificación con Procesos Gaussianos (GPC)

La clase GaussianProcessClassifier implementa GPC para la clasificación probabilística. Coloca una distribución a priori de proceso gaussiano en una función latente, que luego se aplana a través de una función de enlace para obtener las probabilidades de clase. GPC admite la clasificación multi-clase mediante el entrenamiento y la predicción basados en one-versus-rest o one-versus-one.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier
# Crea un modelo GPC con un kernel RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajusta el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Realiza predicciones utilizando el modelo entrenado
y_pred = model.predict(X_test)
```
