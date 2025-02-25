# Importation des bibliothèques requises

Dans cette étape, nous allons importer les bibliothèques nécessaires pour ce tutoriel. Nous allons importer matplotlib, et les bibliothèques pertinentes de mpl_toolkits.axes_grid1.

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
