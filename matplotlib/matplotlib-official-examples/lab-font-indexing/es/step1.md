# Cargar la fuente

En primer lugar, necesitamos cargar un archivo de fuente. En este ejemplo, usaremos el archivo de fuente DejaVuSans.ttf.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
