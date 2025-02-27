# Importez les bibliothèques nécessaires

Tout d'abord, nous devons importer les bibliothèques nécessaires. Nous utiliserons la bibliothèque scikit-learn pour l'apprentissage automatique et le prétraitement des données.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```
