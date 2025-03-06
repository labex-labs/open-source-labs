# Création d'un Jupyter Notebook et préparation des données

Dans cette première étape, nous allons créer un nouveau Jupyter Notebook et préparer nos données pour la visualisation.

## Création d'un nouveau notebook

Dans la première cellule du notebook, importons les bibliothèques nécessaires. Tapez le code suivant et exécutez - le en cliquant sur le bouton "Run" ou en appuyant sur Shift + Enter :

```python
import matplotlib.pyplot as plt
import numpy as np
```

![libraries-imported](../assets/screenshot-20250306-Azb1cb3S@2x.png)

Ce code importe deux bibliothèques essentielles :

- `matplotlib.pyplot` : Une collection de fonctions qui font fonctionner matplotlib comme MATLAB
- `numpy` : Un package fondamental pour le calcul scientifique en Python

## Création de données d'exemple

Maintenant, créons quelques données d'exemple que nous allons visualiser. Dans une nouvelle cellule, entrez et exécutez le code suivant :

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

Lorsque vous exécutez cette cellule, vous devriez voir une sortie similaire à :

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

Les valeurs exactes peuvent varier légèrement. Nous avons créé un ensemble de données avec 10 000 nombres aléatoires générés à partir d'une distribution normale et calculé trois statistiques importantes :

1. Moyenne (μ) : La valeur moyenne de tous les points de données
2. Médiane : La valeur médiane lorsque les données sont triées par ordre croissant
3. Écart - type (σ) : Une mesure de la dispersion des données

Ces statistiques seront utilisées plus tard pour annoter notre visualisation.
