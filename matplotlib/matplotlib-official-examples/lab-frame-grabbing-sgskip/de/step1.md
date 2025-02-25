# Importieren der erforderlichen Bibliotheken

Wir müssen zunächst die erforderlichen Bibliotheken für die Erstellung der Animation importieren. Wir werden `numpy` verwenden, um Zufallszahlen zu generieren, `matplotlib` für die Darstellung und `FFMpegWriter` für das Schreiben der Bilder in eine Datei.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
