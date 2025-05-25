# Aprender Etiquetas com LabelPropagation

Usamos `LabelSpreading` para aprender as etiquetas das amostras desconhecidas.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
