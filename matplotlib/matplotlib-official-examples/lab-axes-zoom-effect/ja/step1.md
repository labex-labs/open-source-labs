# 必要なライブラリのインポート

このステップでは、このチュートリアルに必要なライブラリをインポートします。matplotlibと、mpl_toolkits.axes_grid1からの関連ライブラリをインポートします。

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
