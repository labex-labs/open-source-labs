# 为阴影图显示颜色条

在这一步中，你将学习如何为阴影图显示正确的数字颜色条。

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LightSource, Normalize

def display_colorbar():
    """为阴影图显示正确的数字颜色条。"""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z = 10 * np.cos(x**2 + y**2)

    cmap = plt.cm.copper
    ls = LightSource(315, 45)
    rgb = ls.shade(z, cmap)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')

    # 为颜色条使用代理艺术家……
    im = ax.imshow(z, cmap=cmap)
    im.remove()
    fig.colorbar(im, ax=ax)

    ax.set_title('为阴影图使用颜色条', size='x-large')
```
