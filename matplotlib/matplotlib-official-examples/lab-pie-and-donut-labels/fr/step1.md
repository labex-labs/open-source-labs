# Importez les bibliothèques nécessaires et créez une figure avec des sous-graphiques

Nous commençons par importer les bibliothèques nécessaires et en créant une avec des sous-graphiques.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
