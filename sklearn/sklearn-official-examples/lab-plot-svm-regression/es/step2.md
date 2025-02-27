# Ajustar el modelo de regresión

A continuación, ajustamos un modelo de SVR a nuestro conjunto de datos de muestra usando un kernel lineal, polinomial y RBF. Establecemos los hiperparámetros para cada modelo y los entrenamos en nuestro conjunto de datos de muestra.

```python
from sklearn.svm import SVR

# Fit regression model
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
