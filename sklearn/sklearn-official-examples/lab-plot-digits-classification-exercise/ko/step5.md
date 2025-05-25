# 로지스틱 회귀 분류기를 학습 및 테스트

이제 scikit-learn 의 `LogisticRegression` 함수를 사용하여 로지스틱 회귀 분류기를 학습하고 테스트 세트에서 테스트합니다. 그런 다음 분류기의 정확도 점수를 출력합니다.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
