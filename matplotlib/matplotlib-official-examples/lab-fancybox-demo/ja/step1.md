# ライブラリをインポートしてボックススタイルを取得する

このステップでは、必要なライブラリをインポートし、プロットに使用するボックススタイルを取得します。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```
