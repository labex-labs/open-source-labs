# Train the Label Spreading Model

We train the Label Spreading model with gamma=0.25 and max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```


