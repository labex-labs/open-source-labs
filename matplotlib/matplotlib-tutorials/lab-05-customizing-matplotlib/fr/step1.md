# Configuration des paramètres rc au moment de l'exécution

Vous pouvez modifier dynamiquement les paramètres de configuration par défaut au moment de l'exécution dans un script Python ou de manière interactive à partir de la console Python. La variable `matplotlib.rcParams` est globale au package Matplotlib et stocke tous les paramètres rc. Pour personnaliser les paramètres rc au moment de l'exécution, vous pouvez le modifier directement en utilisant le dictionnaire `mpl.rcParams`. Voici un exemple :

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

Ce code modifie la largeur de ligne et le style de ligne par défaut pour tous les graphiques créés avec Matplotlib.

Voyons quelques données aléatoires tracées avec les nouveaux paramètres par défaut.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
