# Importar as bibliotecas necessárias

Primeiramente, precisamos importar as bibliotecas necessárias para gerar a animação. Usaremos `numpy` para gerar números aleatórios, `matplotlib` para plotar e `FFMpegWriter` para escrever os frames em um arquivo.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
