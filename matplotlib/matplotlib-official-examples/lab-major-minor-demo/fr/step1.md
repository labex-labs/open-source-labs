# Importez les bibliothèques nécessaires et créez des données

```python
import matplotlib.pyplot as plt
import numpy as np

# Créez des données
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

Tout d'abord, nous importons les bibliothèques nécessaires, à savoir Matplotlib et NumPy. Ensuite, nous créons des données pour tracer. Dans cet exemple, nous créons un tableau numpy "t" et calculons un autre tableau numpy "s" à l'aide de t.
