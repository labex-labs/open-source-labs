# 다중 출력 회귀

#### 문제 설명

다중 출력 회귀는 각 샘플에 대한 여러 개의 수치 속성을 예측하는 작업입니다. 각 속성은 수치 변수이며, 속성의 개수는 두 개 이상일 수 있습니다.

#### 대상 형식

다중 출력 회귀 대상의 유효한 표현은 밀집 행렬입니다. 각 행은 샘플을, 각 열은 다른 속성을 나타냅니다.

#### 예제

make_regression 함수를 사용하여 다중 출력 회귀 문제를 생성해 보겠습니다.

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# 다중 출력 회귀 문제 생성
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# 다중 출력 선형 회귀 모델 학습
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# 예측 수행
predictions = model.predict(X)
print(predictions)
```
