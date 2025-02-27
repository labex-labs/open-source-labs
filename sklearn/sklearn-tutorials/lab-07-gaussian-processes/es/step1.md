# Regresión con Procesos Gaussianos (GPR)

La clase GaussianProcessRegressor implementa procesos gaussianos para tareas de regresión. Requiere especificar una distribución a priori para el proceso gaussiano, como las funciones de media y covarianza. Los hiperparámetros del kernel se optimizan durante el proceso de ajuste. Veamos un ejemplo de uso de GPR para la regresión.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Crea un modelo GPR con un kernel RBF
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# Ajusta el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Realiza predicciones utilizando el modelo entrenado
y_pred = model.predict(X_test)
```
