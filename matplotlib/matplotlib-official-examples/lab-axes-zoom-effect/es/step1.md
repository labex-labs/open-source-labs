# Importando las bibliotecas necesarias

En este paso, importaremos las bibliotecas necesarias para este tutorial. Importaremos matplotlib y las bibliotecas relevantes de mpl_toolkits.axes_grid1.

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
