# Carregando o Conjunto de Dados e Criando Pesos de Amostra

Começamos carregando o conjunto de dados e criando alguns pesos de amostra. Usamos a função `make_regression` do scikit-learn para gerar um conjunto de dados de regressão aleatório com 100.000 amostras. Em seguida, geramos um vetor de pesos log-normal e o normalizamos para que a soma seja igual ao número total de amostras.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalizar os pesos de amostra
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
