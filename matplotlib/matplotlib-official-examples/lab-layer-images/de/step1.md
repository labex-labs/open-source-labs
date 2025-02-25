# Importiere erforderliche Bibliotheken und definiere eine Funktion

Importiere die erforderlichen Bibliotheken und definiere eine Funktion, um das erste Bild zu erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
