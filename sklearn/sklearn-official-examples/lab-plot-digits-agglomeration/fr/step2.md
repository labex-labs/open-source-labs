# Chargement de l'ensemble de données

Dans cette étape, nous allons charger l'ensemble de données des chiffres manuscrits à partir de scikit-learn. Cet ensemble de données contient des images de chiffres manuscrits de 0 à 9.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```
