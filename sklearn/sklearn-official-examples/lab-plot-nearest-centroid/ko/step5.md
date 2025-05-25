# 예측 및 정확도 측정

입력 데이터에 대한 클래스 레이블을 예측하고 분류기의 정확도를 측정합니다.

```python
y_pred = clf.predict(X)
print("Accuracy: ", np.mean(y == y_pred))
```
