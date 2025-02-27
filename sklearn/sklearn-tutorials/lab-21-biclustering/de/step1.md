# Importieren der erforderlichen Bibliotheken und des Datensatzes

Zunächst importieren wir die erforderlichen Bibliotheken und laden einen Beispiel-Datensatz, den wir für das Biclustering verwenden werden.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Lade Beispiel-Daten
data = np.arange(100).reshape(10, 10)
```
