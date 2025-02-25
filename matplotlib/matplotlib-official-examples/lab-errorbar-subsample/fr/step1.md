# Importation des bibliothèques et génération de données

Tout d'abord, nous devons importer les bibliothèques nécessaires et générer quelques données d'exemple avec lesquelles travailler. Dans cet exemple, nous utiliserons numpy pour générer les données et matplotlib pour les visualiser.

```python
import matplotlib.pyplot as plt
import numpy as np

# données d'exemple
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# valeurs d'exemple pour les barre d'erreur variables
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
