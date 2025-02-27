# Загрузка данных и определение конвейера

Мы загрузим набор данных digits из scikit-learn и определим конвейер, состоящий из PCA и LinearSVC.

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
