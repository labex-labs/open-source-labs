# 데이터 전처리

StandardScaler 메서드를 사용하여 데이터셋을 스케일링하고 AIC 기준으로 LassoLarsIC 추정기를 맞춥니다.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
