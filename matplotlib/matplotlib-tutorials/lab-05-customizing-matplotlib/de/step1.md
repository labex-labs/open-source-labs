# Die rcParams zur Laufzeit einstellen

Sie können die standardmäßigen Laufzeitkonfigurationsparameter in einem Python-Skript dynamisch ändern oder interaktiv aus der Python-Shell heraus. Die Variable `matplotlib.rcParams` ist global für das Matplotlib-Paket und speichert alle rc-Einstellungen. Um die rcParams zur Laufzeit anzupassen, können Sie sie direkt mithilfe des `mpl.rcParams`-Dictionaries modifizieren. Hier ist ein Beispiel:

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

Dieser Code ändert die standardmäßige Linienbreite und den Linienstil für alle mit Matplotlib erstellten Diagramme.

Schauen wir uns einige zufällige Daten mit den neuen Standardeinstellungen geplottet an.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
