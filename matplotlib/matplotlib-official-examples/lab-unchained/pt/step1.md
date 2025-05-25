# Configuração

Antes de começarmos, precisamos garantir que o Matplotlib esteja instalado. Você pode instalá-lo usando o pip, executando o seguinte comando:

```python
!pip install matplotlib
```

Uma vez instalado, precisamos importar a biblioteca e configurar o ambiente:

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
```
