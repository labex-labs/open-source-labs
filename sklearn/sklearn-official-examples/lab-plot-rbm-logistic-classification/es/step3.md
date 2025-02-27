# Entrenamiento

En este paso, entrenamos el modelo de tubo definido en el paso anterior. Establecemos los hiperparámetros del modelo (tasa de aprendizaje, tamaño de la capa oculta, regularización), y luego ajustamos los datos de entrenamiento al modelo.

```python
from sklearn.base import clone

# Hiper-parámetros. Estos fueron establecidos por validación cruzada,
# utilizando un GridSearchCV. Aquí no estamos realizando validación cruzada para
# ahorrar tiempo.
rbm.learning_rate = 0.06
rbm.n_iter = 10

# Más componentes tienden a dar un mejor rendimiento de predicción, pero mayor
# tiempo de ajuste
rbm.n_components = 100
logistic.C = 6000

# Entrenamiento del Pipeline RBM-Logística
rbm_features_classifier.fit(X_train, Y_train)
```
