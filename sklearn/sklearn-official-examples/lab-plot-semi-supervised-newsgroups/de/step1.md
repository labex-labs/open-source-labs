# Laden des Datensatzes

Wir werden den 20 newsgroups-Datensatz verwenden, der etwa 18.000 Newsgroup-Beiträge zu 20 Themen enthält. In diesem Schritt laden wir den Datensatz und geben einige grundlegende Informationen darüber aus.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Laden des Datensatzes mit den ersten fünf Kategorien
data = fetch_20newsgroups(
    subset="train",
    categories=[
        "alt.atheism",
        "comp.graphics",
        "comp.os.ms-windows.misc",
        "comp.sys.ibm.pc.hardware",
        "comp.sys.mac.hardware",
    ],
)

# Ausgabe von Informationen über den Datensatz
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```
