# 모델 학습

다음으로, 학습 데이터에 회귀 모델을 학습시키겠습니다. 이 예제에서는 Ridge 회귀 모델을 사용합니다.

```python
from sklearn.linear_model import Ridge

# Ridge 회귀 모델 학습
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
