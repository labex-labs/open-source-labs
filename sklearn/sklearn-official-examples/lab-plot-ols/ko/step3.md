# 모델 학습

이제 선형 회귀 객체를 생성하고 학습 데이터셋을 사용하여 모델을 학습합니다.

```python
from sklearn import linear_model

# 선형 회귀 객체 생성
regr = linear_model.LinearRegression()

# 학습 데이터셋을 사용하여 모델 학습
regr.fit(diabetes_X_train, diabetes_y_train)
```
