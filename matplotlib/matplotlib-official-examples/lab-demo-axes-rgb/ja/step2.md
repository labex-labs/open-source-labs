# RGBチャネルを取得する関数を定義する

このステップでは、画像のR、G、Bチャネルを取得するための関数`get_rgb()`を定義します。この例では、`cbook`モジュールの`get_sample_data()`関数を使ってサンプル画像を取得します。

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Get a sample image
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Get R, G, and B channels
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
