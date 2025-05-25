# 이상치 탐지 모델 적용

`LocalOutlierFactor`를 사용하여 이상치 탐지 모델을 적용하고 학습 샘플의 예측 레이블을 계산합니다.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
