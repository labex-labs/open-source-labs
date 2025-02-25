# Lädt die Schriftart

Zunächst müssen wir eine Schriftartdatei laden. In diesem Beispiel verwenden wir die Schriftartdatei DejaVuSans.ttf.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
