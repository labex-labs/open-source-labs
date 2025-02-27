# Clasificación con Procesos Gaussianos (GPC)

La clase GaussianProcessClassifier implementa GPC para la clasificación probabilística. Coloca una distribución a priori de proceso gaussiano en una función latente, que luego se aplana a través de una función de enlace para obtener las probabilidades de clase. GPC admite la clasificación multi-clase mediante el entrenamiento y la predicción basados en one-versus-rest o one-versus-one.

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# Crea un modelo GPC con un kernel RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajusta el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Realiza predicciones utilizando el modelo entrenado
y_pred = model.predict(X_test)
```
