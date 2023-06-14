# Generate Dataset

In this step, we generate the dataset using `make_multilabel_classification` function from `sklearn.datasets`.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```


