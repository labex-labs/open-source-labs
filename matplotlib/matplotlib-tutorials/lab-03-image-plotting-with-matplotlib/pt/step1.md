# Importando Dados de Imagem

Para começar, precisamos importar as bibliotecas necessárias e carregar os dados da imagem em um array NumPy. Em nosso caso, usaremos a biblioteca `PIL` para carregar a imagem e, em seguida, convertê-la em um array NumPy.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
