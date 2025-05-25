# Gerar Dados de Amostra

Primeiro, geramos dados de amostra para usar no nosso problema de regressão. Criamos um array de 40 pontos de dados com 1 característica e, em seguida, criamos um array de destino aplicando a função seno aos dados. Também adicionamos algum ruído a cada 5.º ponto de dados.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Adicionar ruído aos alvos
y[::5] += 1 * (0.5 - np.random.rand(8))
```
