# Préparation des données

Nous commençons par préparer des données fictives avec une relation sinusoidale et du bruit gaussien. Nous utilisons la fonction `linspace()` de Numpy pour créer un tableau 1D de 100 valeurs régulièrement espacées entre 0 et 6. Nous utilisons ensuite l'attribut `np.newaxis` pour convertir le tableau 1D en un tableau 2D de forme `(100,1)`. Nous appliquons la fonction `sin()` à ce tableau et ajoutons une deuxième onde sinusoïdale obtenue en multipliant le tableau par 6. Nous ajoutons ensuite du bruit gaussien avec une moyenne de 0 et une déviation standard de 0,1 en utilisant la fonction `normal()` de Numpy.

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
