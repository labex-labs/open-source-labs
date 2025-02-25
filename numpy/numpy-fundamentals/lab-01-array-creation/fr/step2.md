# Utilisation des fonctions de création de tableaux intrinsèques de NumPy

NumPy fournit des fonctions intégrées pour créer des tableaux. Voici quelques exemples :

```python
import numpy as np

# Créez un tableau 1D avec des valeurs régulièrement incrémentées
arr1D = np.arange(10)

# Créez un tableau 1D avec un type de données spécifique
arr1D_float = np.arange(2, 10, dtype=float)

# Créez un tableau 1D avec un nombre spécifié d'éléments
arr1D_linspace = np.linspace(1., 4., 6)

# Créez une matrice identité 2D
identity_matrix = np.eye(3)

# Créez une matrice 2D avec des valeurs données le long de la diagonale
diag_matrix = np.diag([1, 2, 3])

# Créez une matrice de Vandermonde
vander_matrix = np.vander([1, 2, 3, 4], 2)

# Créez un tableau rempli de zéros
zeros_array = np.zeros((2, 3))

# Créez un tableau rempli de uns
ones_array = np.ones((2, 3))

# Créez un tableau rempli de valeurs aléatoires
random_array = np.random.default_rng(42).random((2, 3))
```
