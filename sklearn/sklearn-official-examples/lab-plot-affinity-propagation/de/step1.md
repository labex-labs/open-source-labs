# Importieren der erforderlichen Bibliotheken

Wir beginnen mit dem Importieren der erforderlichen Bibliotheken, um die Clusteranalyse durchzuführen und Beispiel-Daten zu generieren.

```python
import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
```
