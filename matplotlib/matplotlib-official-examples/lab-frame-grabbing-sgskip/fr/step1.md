# Importez les bibliothèques nécessaires

Nous devons tout d'abord importer les bibliothèques nécessaires pour générer l'animation. Nous utiliserons `numpy` pour générer des nombres aléatoires, `matplotlib` pour tracer et `FFMpegWriter` pour enregistrer les images dans un fichier.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
