# Importieren der erforderlichen Bibliotheken

In diesem Schritt importieren wir die erforderlichen Bibliotheken für dieses Tutorial. Wir importieren matplotlib und die relevanten Bibliotheken aus mpl_toolkits.axes_grid1.

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
