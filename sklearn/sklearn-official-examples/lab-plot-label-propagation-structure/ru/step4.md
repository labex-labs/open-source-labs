# Обучение меток с использованием LabelPropagation

Мы используем `LabelSpreading` для обучения меток неизвестных образцов.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
