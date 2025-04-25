# 必要なライブラリのインポート

このステップでは、このチュートリアルに必要なライブラリをインポートします。matplotlib と、mpl_toolkits.axes_grid1 からの関連ライブラリをインポートします。

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
