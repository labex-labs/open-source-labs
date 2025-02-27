# Bibliotheken importieren

Zunächst müssen wir die erforderlichen Bibliotheken importieren. Wir werden `matplotlib` für die Visualisierung, `datasets` und `metrics` aus `sklearn` verwenden, um den Datensatz zu laden und zu evaluieren, und `svm` für das Training der Support-Vector-Maschine.

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```
