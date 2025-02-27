# Daten generieren

Wir beginnen mit der Datengenerierung. Wir werden das `coins`-Dataset von scikit-image verwenden, das ein 2D-Graustufenbild von Münzen ist. Wir werden das Bild auf 20% seiner ursprünglichen Größe verkleinern, um die Verarbeitung zu beschleunigen.

```python
from skimage.data import coins
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.transform import rescale

orig_coins = coins()

# Verkleinern Sie es auf 20% seiner ursprünglichen Größe, um die Verarbeitung zu beschleunigen
# Anwenden eines Gaußschen Filters zur Glättung vor der Skalierung nach unten
# reduziert Aliasing-Artifakte.

smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(
    smoothened_coins,
    0.2,
    mode="reflect",
    anti_aliasing=False,
)

X = np.reshape(rescaled_coins, (-1, 1))
```
