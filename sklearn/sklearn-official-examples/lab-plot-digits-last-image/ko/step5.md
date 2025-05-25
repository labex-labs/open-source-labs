# 모델 평가

모델의 성능을 평가하기 위해 scikit-learn 의 `accuracy_score` 함수를 사용할 수 있습니다.

```python
from sklearn.metrics import accuracy_score

# 테스트 세트의 레이블 예측
y_pred = clf.predict(X_test)

# 모델의 정확도 계산
accuracy = accuracy_score(y_test, y_pred)

# 모델의 정확도 출력
print("Accuracy:", accuracy)
```
