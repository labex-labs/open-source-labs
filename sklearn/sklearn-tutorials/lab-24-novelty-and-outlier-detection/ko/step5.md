# 이상치 예측

모델이 학습되면 `predict` 메서드를 사용하여 새로운 관측치가 이상치인지 여부를 예측할 수 있습니다. `predict` 메서드는 내부 데이터 (inlier) 에 대해서는 1, 이상치 (outlier) 에 대해서는 -1 을 반환합니다.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
