# Importar Bibliotecas e Gerar Dados

Primeiramente, precisamos importar as bibliotecas necessárias e gerar alguns dados de exemplo para trabalhar. Neste exemplo, usaremos o numpy para gerar os dados e o matplotlib para visualizá-los.

```python
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
