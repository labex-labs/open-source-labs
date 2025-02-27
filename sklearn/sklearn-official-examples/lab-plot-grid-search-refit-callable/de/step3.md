# Daten laden und Pipeline definieren

Wir werden den digits-Datensatz aus scikit-learn laden und eine Pipeline definieren, die aus PCA und LinearSVC besteht.

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
