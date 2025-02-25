# Importer les dépendances

Dans cette étape, nous allons importer les dépendances nécessaires. Nous utiliserons `base64` pour encoder les données d'image, `BytesIO` pour stocker les données d'image en mémoire, `Flask` pour créer le serveur d'application web et `Figure` pour créer les figures.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
