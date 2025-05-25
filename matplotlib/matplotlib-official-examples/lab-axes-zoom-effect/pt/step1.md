# Importando as Bibliotecas Necessárias

Nesta etapa, importaremos as bibliotecas necessárias para este tutorial. Importaremos matplotlib e as bibliotecas relevantes de mpl_toolkits.axes_grid1.

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
