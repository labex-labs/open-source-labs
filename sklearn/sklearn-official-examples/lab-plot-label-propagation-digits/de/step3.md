# Label Spreading-Modell trainieren

Wir trainieren das Label Spreading-Modell mit gamma=0,25 und max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```