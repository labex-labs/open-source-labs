# Normalisierung

Die Normalisierung ist der Prozess, um einzelne Proben so zu skalieren, dass sie eine Einheitsnorm haben. Sie wird häufig verwendet, wenn die Größe der Daten nicht wichtig ist und wir uns nur für die Richtung (oder den Winkel) der Daten interessieren. Wir können den `Normalizer` aus scikit-learn verwenden, um die Normalisierung durchzuführen.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the Normalizer
normalizer = Normalizer()

# Fit and transform the training data
X_normalized = normalizer.fit_transform(X)

# Print the transformed data
print(X_normalized)
```
