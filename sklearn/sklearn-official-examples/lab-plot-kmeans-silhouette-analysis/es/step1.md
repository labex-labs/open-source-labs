# Importar bibliotecas

Comenzaremos importando las bibliotecas necesarias para realizar el análisis.

```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
```
