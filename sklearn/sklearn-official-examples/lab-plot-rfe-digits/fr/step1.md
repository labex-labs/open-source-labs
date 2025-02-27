# Charger l'ensemble de données et diviser les données

Tout d'abord, nous allons charger l'ensemble de données des chiffres à l'aide de la bibliothèque Scikit-Learn. Cet ensemble de données est composé d'images 8x8 de chiffres de 0 à 9. Chaque image est représentée sous forme d'un tableau de 64 caractéristiques. Nous allons diviser les données en variables de caractéristiques et de cible.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```
