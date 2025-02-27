# Erzeugung von Polynommerkmalen

Manchmal ist es vorteilhaft, der Komplexität eines Modells durch die Berücksichtigung nichtlinearer Merkmale der Eingabedaten hinzuzufügen. Wir können die `PolynomialFeatures` aus scikit-learn verwenden, um Polynommerkmale zu erzeugen.

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
