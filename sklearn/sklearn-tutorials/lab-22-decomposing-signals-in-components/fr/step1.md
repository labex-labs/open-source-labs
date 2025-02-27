# Analyse en Composantes Principales (PCA)

#### PCA exacte et interprétation probabiliste

L'Analyse en Composantes Principales (PCA) est utilisée pour décomposer un ensemble de données multivariées en un ensemble de composantes orthogonales successives qui expliquent la plus grande partie de la variance. La PCA peut être implémentée à l'aide de la classe `PCA` de scikit-learn. La méthode `fit` est utilisée pour apprendre les composantes, et la méthode `transform` peut être utilisée pour projeter de nouvelles données sur ces composantes.

```python
from sklearn.decomposition import PCA

# Crée un objet PCA avec n_components comme nombre de composantes souhaitées
pca = PCA(n_components=2)

# Ajuste le modèle PCA aux données
pca.fit(data)

# Transforme les données en les projetant sur les composantes apprises
transformed_data = pca.transform(data)
```
