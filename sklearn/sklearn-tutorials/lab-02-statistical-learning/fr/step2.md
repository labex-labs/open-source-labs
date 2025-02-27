# Redimensionnement des données

Parfois, les données ne sont peut-être pas initialement dans la forme requise par scikit-learn. Dans de tels cas, nous devons prétraiter les données pour les transformer en forme `(n_samples, n_features)`. Un exemple de redimensionnement de données est l'ensemble de données digits, qui est composé de 1797 images 8x8 d'écritures manuscrites de chiffres :

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

Sortie :

```
(1797, 8, 8)
```

Pour utiliser cet ensemble de données avec scikit-learn, nous devons redimensionner chaque image 8x8 en un vecteur de caractéristiques de longueur 64 :

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
