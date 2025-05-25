# 교차 검증 예측 생성

scikit-learn 의 `cross_val_predict` 함수를 사용하여 교차 검증된 예측값을 생성합니다.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
