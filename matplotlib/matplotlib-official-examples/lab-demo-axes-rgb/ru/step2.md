# Определяем функцию для получения RGB-каналов

В этом шаге мы определим функцию `get_rgb()`, которая будет получать каналы R, G и B изображения. В этом примере мы будем использовать функцию `get_sample_data()` из модуля `cbook` для получения образца изображения.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Получаем образец изображения
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Получаем каналы R, G и B
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
