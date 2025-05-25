# Ajustar Regressão Linear Clássica

Agora, ajustaremos os nossos dados usando regressão linear clássica. Isto é feito usando a classe `LinearRegression` do scikit-learn. Em seguida, preveremos os valores para o nosso conjunto de teste e calcularemos a pontuação R2.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
