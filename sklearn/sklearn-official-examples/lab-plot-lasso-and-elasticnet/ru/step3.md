# Automatic Relevance Determination (ARD)

АРД-регрессия представляет собой байесовскую версию Lasso. Она может выдавать интервальные оценки для всех параметров, включая дисперсию ошибки, при необходимости. Это подходящий вариант, когда сигналы имеют гауссовский шум.

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
