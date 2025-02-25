# Импорт необходимых библиотек

В этом шаге мы импортируем необходимые библиотеки для этого руководства. Мы импортируем matplotlib и соответствующие библиотеки из mpl_toolkits.axes_grid1.

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
