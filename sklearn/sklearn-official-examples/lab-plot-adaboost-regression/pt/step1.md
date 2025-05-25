# Preparando os dados

Começamos preparando dados fictícios com uma relação sinusoidal e algum ruído gaussiano. Usamos a função `linspace()` do Numpy para criar um array 1D de 100 valores espaçados uniformemente entre 0 e 6. Em seguida, usamos o atributo `np.newaxis` para converter o array 1D num array 2D com forma `(100,1)`. Aplicamos a função `sin()` a este array e adicionamos uma segunda onda senoidal obtida multiplicando o array por 6. Adicionamos, então, algum ruído gaussiano com média 0 e desvio padrão de 0,1 usando a função `normal()` do Numpy.

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
