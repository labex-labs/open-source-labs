# Bibliotheken und Datensatz importieren

Zunächst müssen wir die erforderlichen Bibliotheken und den Datensatz importieren. In diesem Beispiel werden wir die Bibliotheken `matplotlib` und `mpl_toolkits.mplot3d` verwenden, um den 3D-Graphen zu erstellen, und die Funktion `axes3d.get_test_data()` verwenden, um einen Beispiel-Datensatz zu generieren.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
