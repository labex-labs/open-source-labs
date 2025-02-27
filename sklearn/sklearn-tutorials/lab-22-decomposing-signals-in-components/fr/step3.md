# Factorisation en Matrice Non Négative (NMF)

#### NMF avec la norme de Frobenius

La Factorisation en Matrice Non Négative (NMF) est une approche alternative de décomposition qui suppose des données et des composantes non négatives. Elle trouve une décomposition des données en deux matrices d'éléments non négatifs en optimisant la distance entre les données et le produit matriciel des deux matrices. La NMF peut être implémentée à l'aide de la classe `NMF` de scikit-learn.

```python
from sklearn.decomposition import NMF

# Crée un objet NMF avec n_components comme nombre de composantes souhaitées
nmf = NMF(n_components=2)

# Ajuste le modèle NMF aux données
nmf.fit(data)

# Découpe les données en les deux matrices non négatives
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```
