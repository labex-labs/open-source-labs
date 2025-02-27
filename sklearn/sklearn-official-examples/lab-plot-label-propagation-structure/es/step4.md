# Aprender etiquetas con LabelPropagation

Usamos `LabelSpreading` para aprender las etiquetas de las muestras desconocidas.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
