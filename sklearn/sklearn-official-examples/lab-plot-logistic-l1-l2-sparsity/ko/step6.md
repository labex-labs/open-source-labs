# 희소성 및 점수 계산

각 모델에 대한 희소성 (0 계수의 백분율) 과 점수를 계산합니다.

```python
    coef_l1_LR = clf_l1_LR.coef_.ravel()
    coef_l2_LR = clf_l2_LR.coef_.ravel()
    coef_en_LR = clf_en_LR.coef_.ravel()

    sparsity_l1_LR = np.mean(coef_l1_LR == 0) * 100
    sparsity_l2_LR = np.mean(coef_l2_LR == 0) * 100
    sparsity_en_LR = np.mean(coef_en_LR == 0) * 100

    score_l1_LR = clf_l1_LR.score(X, y)
    score_l2_LR = clf_l2_LR.score(X, y)
    score_en_LR = clf_en_LR.score(X, y)
```
