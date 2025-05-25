# 추정된 모델의 데이터 예측

선형 모델과 RANSAC 회귀 분석기의 데이터를 예측하고 결과를 비교합니다.

```python
# 추정된 모델의 데이터 예측
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
