# Генерация набора данных

В этом шаге мы генерируем набор данных с использованием функции `make_multilabel_classification` из `sklearn.datasets`.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
