# SGD 를 사용한 분류기 학습

이제 SGDClassifier 클래스를 사용하여 분류기를 학습할 것입니다. log_loss 손실 함수와 l2 페널티를 사용할 것입니다.

```python
# SGD 를 사용한 분류기 학습
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# 테스트 세트에서 예측 수행
y_pred = clf.predict(X_test)

# 분류기의 정확도 측정
accuracy = accuracy_score(y_test, y_pred)

# 정확도 출력
print("분류기 정확도:", accuracy)
```
