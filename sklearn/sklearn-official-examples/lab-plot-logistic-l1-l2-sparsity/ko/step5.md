# 서로 다른 페널티와 정규화 매개변수를 사용하여 로지스틱 회귀 모델 학습

L1, L2, 및 탄성 네트 (Elastic-Net) 페널티와 서로 다른 `C` 값을 사용하여 로지스틱 회귀 모델을 학습합니다. 짧은 학습 시간을 위해 허용 오차를 높입니다.

```python
for i, (C, axes_row) in enumerate(zip((1, 0.1, 0.01), axes)):
    clf_l1_LR = LogisticRegression(C=C, penalty="l1", tol=0.01, solver="saga")
    clf_l2_LR = LogisticRegression(C=C, penalty="l2", tol=0.01, solver="saga")
    clf_en_LR = LogisticRegression(C=C, penalty="elasticnet", solver="saga", l1_ratio=l1_ratio, tol=0.01)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)
    clf_en_LR.fit(X, y)
```
