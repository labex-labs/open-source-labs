# 다중 레이블 분류

#### 문제 설명

다중 레이블 분류는 각 샘플이 여러 레이블을 가질 수 있는 분류 작업입니다. 각 샘플이 가질 수 있는 레이블의 수는 두 개보다 큽니다.

#### 대상 형식

다중 레이블 대상의 유효한 표현은 이진 행렬입니다. 각 행은 샘플을, 각 열은 클래스를 나타냅니다. 값 1 은 샘플에 레이블이 존재함을 나타내고, 0 또는 -1 은 존재하지 않음을 나타냅니다.

#### 예제

make_classification 함수를 사용하여 다중 레이블 분류 문제를 생성해 보겠습니다.

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# 다중 레이블 분류 문제 생성
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# 다중 출력 랜덤 포레스트 분류기 학습
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# 예측 수행
predictions = model.predict(X)
print(predictions)
```
