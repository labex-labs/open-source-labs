# Importation des données d'image

Pour commencer, nous devons importer les bibliothèques nécessaires et charger les données d'image dans un tableau NumPy. Dans notre cas, nous utiliserons la bibliothèque `PIL` pour charger l'image, puis la convertir en un tableau NumPy.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
