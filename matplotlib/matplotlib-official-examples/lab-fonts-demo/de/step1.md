# Einrichten

Bevor wir beginnen, müssen wir die erforderlichen Bibliotheken importieren und das Diagramm einrichten.

```python
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure()
alignment = {'horizontalalignment': 'center','verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
heading_font = FontProperties(size='large')
```
