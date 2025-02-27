# Lasso

В этом шаге мы покажем, как использовать модель Lasso-регрессии для оценки разреженных коэффициентов датасета. Мы будем использовать фиксированное значение параметра регуляризации `alpha`. На практике оптимальный параметр `alpha` должен быть выбран путём передачи стратегии кросс-валидации `TimeSeriesSplit` в `LassoCV`. Чтобы сделать пример простым и быстро исполняемым, мы здесь напрямую задаём оптимальное значение для alpha.

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"Lasso fit done in {(time() - t0):.3f}s")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso r^2 on test data : {r2_score_lasso:.3f}")
```
