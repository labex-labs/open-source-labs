# Lade das Dataset

Wir werden das 20 newsgroups-Dataset verwenden, das ungefähr 18.000 Newsgroup-Posts zu 20 Themen enthält. In diesem Schritt werden wir das Dataset laden und einige grundlegende Informationen darüber ausgeben.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Lade das Dataset mit den ersten fünf Kategorien
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

# Gib Informationen über das Dataset aus
print("%d Dokumente" % len(data.filenames))
print("%d Kategorien" % len(data.target_names))
```