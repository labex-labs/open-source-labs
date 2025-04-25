# numpy 配列を Pillow 画像に保存する

numpy 配列ができたので、それを Pillow に渡して、Pillow がサポートする任意の形式で保存することができます。この例では、グラフを BMP 画像として保存します。

```python
from PIL import Image

im = Image.fromarray(rgba)
im.save("test.bmp")
```
