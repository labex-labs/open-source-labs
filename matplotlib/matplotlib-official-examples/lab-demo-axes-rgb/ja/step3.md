# RGB キューブを作成する関数を定義する

このステップでは、前のステップで取得した R、G、B チャネルから RGB キューブを作成する関数`make_cube()`を定義します。この関数は、R、G、B キューブと RGB 画像を返します。

```python
def make_cube(r, g, b):
    # Get the shape of R
    ny, nx = r.shape

    # Create the R, G, and B cubes
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Combine the R, G, and B cubes to create the RGB image
    RGB = R + G + B

    return R, G, B, RGB
```
