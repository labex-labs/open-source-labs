# Charger les données

Tout d'abord, nous chargeons l'ensemble de données des chiffres (digits dataset) de scikit-learn. Cet ensemble de données contient des images 8x8 de chiffres allant de 0 à 9. Nous utiliserons l'Analyse en Composantes Principales (Principal Component Analysis - PCA) pour réduire la dimension de l'ensemble de données à 15.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# charger l'ensemble de données des chiffres
digits = load_digits()

# réduire la dimension de l'ensemble de données à 15 en utilisant la PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
