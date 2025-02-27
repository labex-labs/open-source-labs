# Выбор Lasso с использованием критерия информативности

Мы будем использовать функцию `LassoLarsIC` из `sklearn.linear_model`, чтобы получить оценщик Lasso, который использует критерий информационного качества Акаике (AIC) или критерий Байеса (BIC) для выбора оптимального значения параметра регуляризации alpha. Сначала мы обучим модель Lasso с использованием критерия AIC.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
