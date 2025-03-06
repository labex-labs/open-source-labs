# Comprendre Matplotlib et créer un notebook

Dans cette première étape, nous allons apprendre à connaître Matplotlib et créer un nouveau notebook Jupyter pour notre tâche de visualisation.

## Qu'est-ce que Matplotlib ?

Matplotlib est une bibliothèque complète pour créer des visualisations statiques, animées et interactives en Python. Elle fournit une API orientée objet pour intégrer des graphiques dans des applications et est largement utilisée pour la visualisation de données par les scientifiques, les ingénieurs et les analystes de données.

## Créer un nouveau notebook

Dans la première cellule de votre notebook, importons la bibliothèque Matplotlib. Tapez le code suivant et exécutez la cellule en appuyant sur Shift+Enter :

```python
import matplotlib.pyplot as plt
import numpy as np

# Check the Matplotlib version
print(f"NumPy version: {np.__version__}")
```

![libraries-imported](../assets/screenshot-20250306-K6iIFfj1@2x.png)

Lorsque vous exécutez ce code, vous devriez voir une sortie similaire à :

```
NumPy version: 2.0.0
```

Le numéro de version exact peut varier en fonction de votre environnement.

Maintenant, nous avons importé Matplotlib et il est prêt à être utilisé. `plt` est un alias conventionnel utilisé pour le module pyplot, qui fournit une interface similaire à MATLAB pour créer des graphiques.
