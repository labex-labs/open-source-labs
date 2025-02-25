# Créer des données de test

Tout d'abord, nous allons créer quelques données de test pour les utiliser dans le diagramme à violon. Nous utiliserons NumPy pour générer quatre tableaux de 100 valeurs distribuées normalement avec des écarts-types croissants.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
