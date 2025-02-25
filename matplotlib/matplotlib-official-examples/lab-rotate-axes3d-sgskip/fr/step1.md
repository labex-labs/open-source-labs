# Importation des bibliothèques et de l'ensemble de données

Tout d'abord, nous devons importer les bibliothèques et l'ensemble de données nécessaires. Dans cet exemple, nous utiliserons les bibliothèques `matplotlib` et `mpl_toolkits.mplot3d` pour créer le tracé 3D, et la fonction `axes3d.get_test_data()` pour générer un ensemble de données d'échantillonnage.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Générer un ensemble de données d'échantillonnage
X, Y, Z = axes3d.get_test_data(0.05)
```
