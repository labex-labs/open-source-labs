# 画像データの定義

サンプルの画像データとその範囲を返す関数を定義します。

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
