# Gerar Dados

Começamos gerando o conjunto de dados Swiss Roll usando a função `make_swiss_roll` da Scikit-learn. O conjunto de dados Swiss Roll é um conjunto de dados 3D com forma de espiral.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Torná-lo mais fino
X[:, 1] *= 0.5
```
