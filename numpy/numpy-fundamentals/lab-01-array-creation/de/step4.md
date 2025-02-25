# Einlesen von Arrays von der Festplatte

Sie können Arrays von der Festplatte in verschiedenen Formaten einlesen. Für standardmäßige binäre Formate gibt es Python-Bibliotheken wie h5py für HDF5 und Astropy für FITS. Für übliche ASCII-Formate wie CSV und TSV können Sie die Funktionen `np.loadtxt` und `np.genfromtxt` verwenden. Hier ist ein Beispiel zum Einlesen einer CSV-Datei:

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
