# Learn Labels with LabelPropagation

We use `LabelSpreading` to learn the labels of the unknown samples.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
