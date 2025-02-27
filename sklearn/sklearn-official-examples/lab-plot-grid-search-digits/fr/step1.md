# Charger les données

Nous allons charger l'ensemble de données digits et aplatir les images en vecteurs. Chaque image de 8 pixels sur 8 doit être transformée en un vecteur de 64 pixels. Ainsi, nous obtiendrons un tableau de données final de forme `(n_images, n_pixels)`. Nous allons également diviser les données en un ensemble d'entraînement et un ensemble de test de taille égale.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
