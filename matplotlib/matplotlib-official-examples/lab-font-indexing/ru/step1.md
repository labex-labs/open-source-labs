# Загрузка шрифта

Во - первых, нам нужно загрузить файл шрифта. В этом примере мы будем использовать файл шрифта DejaVuSans.ttf.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
