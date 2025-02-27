# Применение классической линейной регрессии

Теперь мы применим классическую линейную регрессию к нашим данным. Это делается с использованием класса `LinearRegression` из scikit-learn. Затем мы предскажем значения для нашей тестовой выборки и вычислим показатель R2.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
