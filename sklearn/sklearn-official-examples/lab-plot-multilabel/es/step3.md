# Generar el conjunto de datos

En este paso, generamos el conjunto de datos utilizando la función `make_multilabel_classification` de `sklearn.datasets`.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
