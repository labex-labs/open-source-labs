# 新しいサンプルの生成

このステップでは、新しいサンプルを生成し、元のデータセットとともにプロットします。再度、`make_blobs`関数を使って 10 個の新しいサンプルを生成します。

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```
