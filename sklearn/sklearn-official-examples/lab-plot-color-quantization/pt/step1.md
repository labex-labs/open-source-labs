# Carregar e Exibir a Imagem Original

Começaremos carregando e exibindo a imagem original do Palácio de Verão.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# Carregar a foto do Palácio de Verão
china = load_sample_image("china.jpg")

# Exibir a imagem original
plt.figure()
plt.axis("off")
plt.title("Imagem Original")
plt.imshow(china)
plt.show()
```
