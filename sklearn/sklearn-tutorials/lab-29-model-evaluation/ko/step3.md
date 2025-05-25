# 메트릭 함수

Scikit-learn `metrics` 모듈은 특정 목적에 맞는 예측 오류를 평가하기 위한 여러 함수를 구현합니다. 이 함수들을 사용하여 모델이 만든 예측의 품질을 계산할 수 있습니다.

`metrics` 모듈의 `accuracy_score` 함수 사용 예는 다음과 같습니다.

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
