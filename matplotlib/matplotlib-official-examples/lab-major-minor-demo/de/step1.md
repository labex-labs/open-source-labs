# Importieren der erforderlichen Bibliotheken und Erstellen von Daten

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

Zunächst importieren wir die erforderlichen Bibliotheken, nämlich Matplotlib und NumPy. Anschließend erstellen wir die Daten, die geplottet werden sollen. In diesem Beispiel erstellen wir ein numpy-Array "t" und berechnen mithilfe von t ein weiteres numpy-Array "s".
