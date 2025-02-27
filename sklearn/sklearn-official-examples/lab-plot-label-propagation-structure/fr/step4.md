# Apprendre les étiquettes avec LabelPropagation

Nous utilisons `LabelSpreading` pour apprendre les étiquettes des échantillons inconnus.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
