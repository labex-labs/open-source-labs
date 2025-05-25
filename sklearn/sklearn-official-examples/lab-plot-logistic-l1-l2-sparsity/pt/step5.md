# Treinar Modelos de Regressão Logística com Diferentes Penalidades e Parâmetros de Regularização

Treinaremos modelos de regressão logística com penalidades L1, L2 e Elastic-Net e diferentes valores de `C`. Aumentaremos a tolerância para reduzir o tempo de treinamento.

```python
for i, (C, axes_row) in enumerate(zip((1, 0.1, 0.01), axes)):
    clf_l1_LR = LogisticRegression(C=C, penalty="l1", tol=0.01, solver="saga")
    clf_l2_LR = LogisticRegression(C=C, penalty="l2", tol=0.01, solver="saga")
    clf_en_LR = LogisticRegression(C=C, penalty="elasticnet", solver="saga", l1_ratio=l1_ratio, tol=0.01)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)
    clf_en_LR.fit(X, y)
```
