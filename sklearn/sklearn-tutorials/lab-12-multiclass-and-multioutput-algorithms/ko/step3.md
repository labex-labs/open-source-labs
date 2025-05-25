# 다중 클래스 - 다중 출력 분류

#### 문제 설명

다중 클래스 - 다중 출력 분류 (또는 다중 작업 분류) 는 각 샘플에 대한 여러 개의 이진이 아닌 속성을 예측하는 작업입니다. 각 속성은 두 개 이상의 클래스를 가질 수 있습니다.

#### 대상 형식

다중 클래스 - 다중 출력 대상의 유효한 표현은 밀집 행렬입니다. 각 행은 샘플을, 각 열은 다른 속성 또는 클래스를 나타냅니다.

#### 예제

make_classification 함수를 사용하여 다중 클래스 - 다중 출력 분류 문제를 생성해 보겠습니다.

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# 다중 클래스 - 다중 출력 분류 문제 생성
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# 다중 출력 서포트 벡터 분류기 학습
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# 예측 수행
predictions = model.predict(X)
print(predictions)
```
