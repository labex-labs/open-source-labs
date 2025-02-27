# Labels mit LabelPropagation lernen

Wir verwenden `LabelSpreading`, um die Labels der unbekannten Proben zu lernen.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
