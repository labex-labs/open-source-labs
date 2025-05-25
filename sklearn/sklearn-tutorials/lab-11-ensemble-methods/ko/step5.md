# Bagging 분류기 평가

`score` 메서드를 사용하여 테스트 데이터에 대한 정확도 점수를 계산하여 Bagging 분류기를 평가해 보겠습니다.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```
