# Charger la police

Tout d'abord, nous devons charger un fichier de police. Dans cet exemple, nous utiliserons le fichier de police DejaVuSans.ttf.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
