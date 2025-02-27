# Entraîner des modèles de régression logistique avec différentes pénalités et paramètres de régularisation

Nous allons entraîner des modèles de régression logistique avec des pénalités L1, L2 et Elastic-Net et différentes valeurs de `C`. Nous augmenterons la tolérance pour réduire le temps d'entraînement.

```python
for i, (C, axes_row) in enumerate(zip((1, 0.1, 0.01), axes)):
    clf_l1_LR = LogisticRegression(C=C, penalty="l1", tol=0.01, solver="saga")
    clf_l2_LR = LogisticRegression(C=C, penalty="l2", tol=0.01, solver="saga")
    clf_en_LR = LogisticRegression(C=C, penalty="elasticnet", solver="saga", l1_ratio=l1_ratio, tol=0.01)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)
    clf_en_LR.fit(X, y)
```
