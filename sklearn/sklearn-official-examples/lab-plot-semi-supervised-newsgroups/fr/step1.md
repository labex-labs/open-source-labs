# Charger l'ensemble de données

Nous utiliserons l'ensemble de données 20 newsgroups, qui contient environ 18 000 messages de newsgroup sur 20 sujets. Dans cette étape, nous allons charger l'ensemble de données et afficher quelques informations de base à son sujet.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Charger l'ensemble de données avec les cinq premières catégories
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

# Afficher des informations sur l'ensemble de données
print("%d documents" % len(data.filenames))
print("%d catégories" % len(data.target_names))
```
