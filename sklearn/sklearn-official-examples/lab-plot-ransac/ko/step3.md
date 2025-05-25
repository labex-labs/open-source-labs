# RANSAC 회귀 분석기 적합

scikit-learn 의 `RANSACRegressor` 클래스를 사용하여 데이터에 RANSAC 회귀 분석기를 적합합니다.

```python
# RANSAC 알고리즘으로 강건하게 선형 모델 적합
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
