# データの読み込みとパイプラインの定義

scikit-learn から digits データセットを読み込み、PCA と LinearSVC から構成されるパイプラインを定義します。

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
