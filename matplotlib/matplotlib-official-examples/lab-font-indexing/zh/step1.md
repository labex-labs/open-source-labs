# 加载字体

首先，我们需要加载一个字体文件。在这个例子中，我们将使用 DejaVuSans.ttf 字体文件。

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
