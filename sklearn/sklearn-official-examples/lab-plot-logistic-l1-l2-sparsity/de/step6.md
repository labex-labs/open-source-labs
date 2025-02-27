# Berechnung der Sparsität und der Scores

Wir werden die Sparsität (Prozentsatz der Koeffizienten, die Null sind) und die Scores für jedes Modell berechnen.

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
