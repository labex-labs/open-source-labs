# Importieren der erforderlichen Bibliotheken

Wir müssen die Matplotlib- und NumPy-Bibliotheken importieren, um das Streudiagramm auf einer polaren Achse zu erstellen. Wir setzen auch den Zufallszahlengenerator, um die Reproduzierbarkeit zu gewährleisten.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```
