# Mínimos Cuadrados Ordinarios

> Comience con [Aprendizaje Supervisado: Regresión](https://labex.io/courses/supervised-learning-regression), si no tiene experiencia previa en Aprendizaje Automático.

Los Mínimos Cuadrados Ordinarios (OLS) es un método de regresión lineal que minimiza la suma de las diferencias al cuadrado entre los objetivos observados y los objetivos predichos. Matemáticamente, resuelve un problema de la forma:
$$\min_{w} || X w - y||_2^2$$

Comencemos ajustando un modelo de regresión lineal utilizando OLS.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- Importamos el módulo `linear_model` de scikit-learn.
- Creamos una instancia de `LinearRegression`.
- Utilizamos el método `fit` para ajustar el modelo a los datos de entrenamiento.
- Imprimimos los coeficientes del modelo lineal.
