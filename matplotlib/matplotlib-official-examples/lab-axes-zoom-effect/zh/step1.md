# 导入所需库

在这一步中，我们将导入本教程所需的必要库。我们将导入 matplotlib 以及 mpl_toolkits.axes_grid1 中的相关库。

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
