# Créez des données d'échantillonnage

Ensuite, nous devons créer quelques données d'échantillonnage pour ajuster notre modèle de régression isotone. Dans cet exemple, nous allons générer deux tableaux, `X` et `y`, représentant respectivement les données d'entrée et les valeurs cibles.

```python
import numpy as np

# Génère des données d'entrée aléatoires
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
