# 다중 클래스 분류

#### 문제 설명

다중 클래스 분류는 두 개 이상의 클래스가 있는 분류 작업입니다. 각 샘플은 하나의 클래스에만 할당됩니다.

#### 대상 형식

다중 클래스 대상의 유효한 표현은 두 개 이상의 이산 값을 포함하는 1 차원 또는 열 벡터입니다.

#### 예제

붓꽃 데이터셋을 사용하여 다중 클래스 분류를 보여줍니다.

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# 붓꽃 데이터셋 로드
X, y = datasets.load_iris(return_X_y=True)

# OneVsRestClassifier 를 사용하여 로지스틱 회귀 모델 학습
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# 예측 수행
predictions = model.predict(X)
print(predictions)
```
