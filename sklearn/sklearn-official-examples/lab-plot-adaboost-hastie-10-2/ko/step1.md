# 데이터 준비 및 기본 모델

Hastie 등 (2009) 의 예제 10.2 에서 사용된 이진 분류 데이터셋을 생성합니다. 그런 다음 AdaBoost 분류기의 하이퍼파라미터를 설정합니다. 데이터를 학습 세트와 테스트 세트로 분할합니다. 그 후, `DecisionTreeClassifier` (깊이=9) 와 `DecisionTreeClassifier` (깊이=1, "stump") 기본 분류기를 학습하고 테스트 오류를 계산합니다.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.make_hastie_10_2(n_samples=12_000, random_state=1)

n_estimators = 400
learning_rate = 1.0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=2_000, shuffle=False
)

dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
dt_stump.fit(X_train, y_train)
dt_stump_err = 1.0 - dt_stump.score(X_test, y_test)

dt = DecisionTreeClassifier(max_depth=9, min_samples_leaf=1)
dt.fit(X_train, y_train)
dt_err = 1.0 - dt.score(X_test, y_test)
```
