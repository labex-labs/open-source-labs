# Применение неотрицательных наименьших квадратов для регрессии

Теперь мы применим неотрицательные наименьшие квадраты для регрессии к нашим данным. Это делается с использованием класса `LinearRegression` из scikit-learn с параметром `positive=True`. Затем мы предскажем значения для нашей тестовой выборки и вычислим показатель R2.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
