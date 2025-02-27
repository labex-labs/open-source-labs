# Regresión Lineal

En este paso, exploraremos el concepto de regresión lineal y cómo se puede implementar utilizando scikit-learn. Utilizaremos el conjunto de datos de diabetes, que consta de variables fisiológicas de pacientes y su evolución de la enfermedad después de un año.

#### Cargar el Conjunto de Datos de Diabetes

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Crear y Ajustar un Modelo de Regresión Lineal

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Hacer Predicciones y Calcular Métricas de Rendimiento

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
