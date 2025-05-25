# Importar as Bibliotecas Necessárias

Começaremos importando as bibliotecas necessárias. Usaremos Matplotlib, NumPy e StringIO para este exemplo.

```python
from contextlib import ExitStack
from matplotlib.axes import Axes
import matplotlib.axis as maxis
from matplotlib.projections import register_projection
import matplotlib.spines as mspines
import matplotlib.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from matplotlib.ticker import (MultipleLocator, NullFormatter, ScalarFormatter)
```
