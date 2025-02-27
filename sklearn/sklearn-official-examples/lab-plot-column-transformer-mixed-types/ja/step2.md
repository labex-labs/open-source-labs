# データセットの読み込み

このステップでは、`fetch_openml` を使って OpenML からタイタニック号のデータセットを読み込みます。

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
