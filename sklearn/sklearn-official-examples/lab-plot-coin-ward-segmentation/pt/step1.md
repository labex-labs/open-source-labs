# Gerar Dados

Começaremos gerando os dados. Usaremos o conjunto de dados `coins` do scikit-image, que é uma imagem 2D em escala de cinza de moedas. Redimensionaremos a imagem para 20% do tamanho original para acelerar o processamento.

```python
from skimage.data import coins
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.transform import rescale

orig_coins = coins()

# Redimensioná-la para 20% do tamanho original para acelerar o processamento.
# Aplicar um filtro Gaussiano para suavização antes da redução de escala
# reduz artefatos de aliasing.

smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(
    smoothened_coins,
    0.2,
    mode="reflect",
    anti_aliasing=False,
)

X = np.reshape(rescaled_coins, (-1, 1))
```
