# Aktivieren von Copy-On-Write

Zunächst aktivieren wir CoW in pandas. Dies kann mit der `copy_on_write`-Konfigurationsoption in pandas erreicht werden. Hier sind zwei Möglichkeiten, CoW global zu aktivieren.

```python
# Importieren der pandas- und numpy-Bibliotheken
import pandas as pd

# CoW mit set_option aktivieren
pd.set_option("mode.copy_on_write", True)

# Oder mit direkter Zuweisung
pd.options.mode.copy_on_write = True
```
