# Ajustar o Modelo de Regressão

Em seguida, ajustamos um modelo SVR ao nosso conjunto de dados de amostra usando um kernel linear, polinomial e RBF. Definimos os hiperparâmetros para cada modelo e os treinamos no nosso conjunto de dados de amostra.

```python
from sklearn.svm import SVR

# Ajustar o modelo de regressão
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
