# 모델 개선

모델의 정확도가 만족스럽지 않다면 SVM 알고리즘의 하이퍼파라미터를 조정하여 개선해 볼 수 있습니다. 예를 들어, `C` 매개변수의 값을 변경해 볼 수 있습니다.

```python
# 다른 C 값으로 SVM 분류기를 생성
clf = SVC(kernel='linear', C=0.1)

# 학습 데이터로 분류기를 학습
clf.fit(X_train, y_train)

# 테스트 세트의 레이블 예측
y_pred = clf.predict(X_test)

# 모델의 정확도 계산
accuracy = accuracy_score(y_test, y_pred)

# 모델의 정확도 출력
print("Accuracy:", accuracy)
```
