# Gerar Dados de Amostra

Primeiro, geramos um conjunto de dados de amostra composto por 40 valores aleatórios entre 0 e 5. Em seguida, calculamos a função seno de cada valor e adicionamos algum ruído a cada 5º valor.

```python
import numpy as np

# Gerar dados de amostra
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# adicionar ruído aos alvos
y[::5] += 3 * (0.5 - np.random.rand(8))
```
