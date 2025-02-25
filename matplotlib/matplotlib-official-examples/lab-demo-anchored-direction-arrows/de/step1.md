# Importieren der erforderlichen Bibliotheken

Zunächst müssen wir die erforderlichen Bibliotheken wie Matplotlib, NumPy, den Matplotlib-Schriftmanager und AnchoredDirectionArrows aus mpl_toolkits.axes_grid1 importieren. Wir werden diese Bibliotheken verwenden, um ankergestützte Richtungsarrows zu erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows
```
