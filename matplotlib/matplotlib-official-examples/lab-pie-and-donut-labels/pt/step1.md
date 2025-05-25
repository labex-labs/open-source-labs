# Importar as bibliotecas necessárias e criar uma figura com subplots

Começamos importando as bibliotecas necessárias e criando uma figura com subplots.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
