# Créer un objet Triangulation

Tout d'abord, nous devons créer un objet Triangulation. Nous allons utiliser la classe `Triangulation` de `matplotlib.tri`. Dans cet exemple, nous allons créer un objet Triangulation avec des données aléatoires.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Générer des données aléatoires
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
