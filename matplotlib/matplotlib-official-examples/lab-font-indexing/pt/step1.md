# Carregar a Fonte

Primeiramente, precisamos carregar um arquivo de fonte. Neste exemplo, usaremos o arquivo de fonte DejaVuSans.ttf.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
