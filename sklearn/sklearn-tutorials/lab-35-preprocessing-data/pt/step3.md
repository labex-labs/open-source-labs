# Normalização

A normalização é o processo de escalonar amostras individuais para ter norma unitária. É comumente usada quando a magnitude dos dados não é importante e estamos apenas interessados na direção (ou ângulo) dos dados. Podemos usar o `Normalizer` do scikit-learn para realizar a normalização.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Cria um conjunto de dados de amostra
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Inicializa o Normalizer
normalizer = Normalizer()

# Ajusta e transforma os dados de treinamento
X_normalized = normalizer.fit_transform(X)

# Imprime os dados transformados
print(X_normalized)
```
