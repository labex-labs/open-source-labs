# Importar las bibliotecas necesarias y crear una figura con subgráficos

Comenzamos importando las bibliotecas necesarias y creando una figura con subgráficos.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
