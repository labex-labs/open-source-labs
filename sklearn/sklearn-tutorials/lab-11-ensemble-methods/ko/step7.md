# 랜덤 포레스트 분류기 평가

테스트 데이터에 대한 정확도 점수를 계산하여 랜덤 포레스트 분류기를 평가해 보겠습니다.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Random Forest Classifier Accuracy: {accuracy}")
```
