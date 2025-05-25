# 레이블 확산 모델 학습

gamma=0.25 및 max_iter=20 으로 레이블 확산 모델을 학습합니다.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
