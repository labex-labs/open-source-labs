# 선형 회귀

이 단계에서는 선형 회귀의 개념과 scikit-learn 을 사용하여 구현하는 방법을 탐색합니다. 환자의 생리학적 변수와 1 년 후 질병 진행 상황으로 구성된 당뇨병 데이터셋을 사용할 것입니다.

#### 당뇨병 데이터셋 로드

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### 선형 회귀 모델 생성 및 학습

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### 예측 수행 및 성능 지표 계산

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
