# 가우시안 나이브 베이즈 분류기 학습 및 평가

이제 학습 세트에서 가우시안 나이브 베이즈 분류기를 학습하고 테스트 세트에서 성능을 평가합니다. `sklearn.naive_bayes` 모듈의 `GaussianNB` 클래스를 사용합니다.

```python
from sklearn.naive_bayes import GaussianNB

# 가우시안 나이브 베이즈 분류기 생성
gnb = GaussianNB()

# 분류기 학습
gnb.fit(X_train, y_train)

# 테스트 세트에 대한 목표 변수 예측
y_pred = gnb.predict(X_test)

# 분류기의 정확도 계산
accuracy = (y_pred == y_test).sum() / len(y_test)
print("정확도:", accuracy)
```
