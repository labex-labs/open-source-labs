# Importar Bibliotecas e Configurar o Gráfico

O primeiro passo é importar as bibliotecas necessárias e configurar o gráfico. Neste exemplo, usaremos o módulo `pyplot` do Matplotlib e seu toolkit `3d` para criar o gráfico 3D.

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
