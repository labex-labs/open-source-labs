# Dataset et modèle

Nous utiliserons le jeu de données iris et un classifieur Linear SVC pour différencier deux types d'iris. Tout d'abord, nous importerons les bibliothèques nécessaires et chargerons le jeu de données.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

Ensuite, nous ajouterons des caractéristiques bruitées au jeu de données et le diviserons en ensembles d'entraînement et de test.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

Enfin, nous mettrons à l'échelle les données à l'aide d'un StandardScaler et ajusterons un classifieur Linear SVC aux données d'entraînement.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
