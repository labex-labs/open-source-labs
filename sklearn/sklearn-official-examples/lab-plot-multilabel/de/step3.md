# Datensatz generieren

In diesem Schritt generieren wir den Datensatz mit der Funktion `make_multilabel_classification` aus `sklearn.datasets`.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
