# デモ画像を取得する

このステップでは、デモ画像とその範囲を取得する関数を定義します。サンプル画像を取得するために、`cbook` から `get_sample_data()` 関数を使用します。

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
