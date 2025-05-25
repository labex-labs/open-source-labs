# 평가 매개변수

Scikit-learn 은 교차 검증 및 그리드 검색과 같은 여러 모델 평가 도구에서 `scoring` 매개변수를 제공합니다. `scoring` 매개변수는 평가 중 추정기에 적용되는 메트릭을 제어합니다.

교차 검증에서 `scoring` 매개변수를 사용하는 예는 다음과 같습니다.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
