# フォントの読み込み

まず、フォントファイルを読み込む必要があります。この例では、DejaVuSans.ttf フォントファイルを使用します。

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
