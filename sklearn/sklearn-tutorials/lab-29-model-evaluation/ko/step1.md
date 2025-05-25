# 추정기 점수 메서드

추정기 점수 메서드는 각 추정기에서 scikit-learn 이 제공하는 기본 평가 기준입니다. 모델 예측의 품질을 나타내는 점수를 계산합니다. 각 추정기의 설명서에서 자세한 내용을 확인할 수 있습니다.

추정기의 `score` 메서드 사용 예시는 다음과 같습니다.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
