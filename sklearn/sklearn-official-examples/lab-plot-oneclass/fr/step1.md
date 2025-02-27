# Importez les bibliothèques nécessaires et générez des données

La première étape consiste à importer les bibliothèques nécessaires et à générer des données. Nous utiliserons numpy et matplotlib pour générer et visualiser les données, et scikit-learn pour construire le modèle de SVM à une classe.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Générez les données d'entraînement
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Générez quelques observations nouvelles régulières
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Générez quelques observations nouvelles anormales
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
