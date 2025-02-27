# Генерация данных

Начнем с генерации данных. Будем использовать датасет `coins` из scikit-image, который представляет собой 2D-граayscale изображение монет. Изменим размер изображения до 20% от исходного, чтобы ускорить обработку.

```python
from skimage.data import coins
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.transform import rescale

orig_coins = coins()

# Resize it to 20% of the original size to speed up the processing
# Applying a Gaussian filter for smoothing prior to down-scaling
# reduces aliasing artifacts.

smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(
    smoothened_coins,
    0.2,
    mode="reflect",
    anti_aliasing=False,
)

X = np.reshape(rescaled_coins, (-1, 1))
```
