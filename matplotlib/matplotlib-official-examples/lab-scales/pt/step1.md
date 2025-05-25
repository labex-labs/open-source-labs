# Importar Bibliotecas e Gerar Dados

Primeiro, precisamos importar as bibliotecas necessárias e gerar alguns dados para plotar. Neste exemplo, usaremos uma distribuição normal para gerar dados para o eixo y.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```
