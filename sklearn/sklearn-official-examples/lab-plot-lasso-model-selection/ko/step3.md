# 정보 기준을 통한 Lasso 선택

`sklearn.linear_model`의 `LassoLarsIC` 함수를 사용하여 Akaike 정보 기준 (AIC) 또는 Bayes 정보 기준 (BIC) 을 사용하여 정규화 매개변수 alpha 의 최적 값을 선택하는 Lasso 추정기를 제공합니다. 먼저 AIC 기준으로 Lasso 모델을 맞출 것입니다.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
