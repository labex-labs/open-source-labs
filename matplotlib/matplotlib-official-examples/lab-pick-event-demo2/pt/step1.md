# Gerar Dados Aleatórios

Primeiramente, precisamos gerar 100 conjuntos de dados aleatórios, cada um contendo 1000 números aleatórios entre 0 e 1. Usaremos o módulo `random` do numpy para gerar os dados aleatórios.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
