# Importation des bibliothèques et configuration du tracé

La première étape consiste à importer les bibliothèques nécessaires et à configurer le tracé. Dans cet exemple, nous utiliserons le module `pyplot` de Matplotlib et son outil de tracé en 3D pour créer le tracé en 3D.

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
