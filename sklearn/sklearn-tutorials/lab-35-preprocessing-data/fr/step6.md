# Génération de caractéristiques polynômes

Parfois, il est avantageux d'ajouter de la complexité à un modèle en considérant les caractéristiques non linéaires des données d'entrée. Nous pouvons utiliser `PolynomialFeatures` de scikit-learn pour générer des caractéristiques polynômes.

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Create a sample dataset
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# Initialize the PolynomialFeatures
poly = PolynomialFeatures(2)

# Fit and transform the training data
X_poly = poly.fit_transform(X)

# Print the transformed data
print(X_poly)
```
