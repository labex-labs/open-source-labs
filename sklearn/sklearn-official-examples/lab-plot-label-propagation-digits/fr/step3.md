# Entraîner le modèle Label Spreading

Nous entraînons le modèle Label Spreading avec gamma=0,25 et max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
