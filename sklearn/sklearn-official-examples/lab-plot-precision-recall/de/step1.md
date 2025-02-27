# Dataset und Modell

Wir werden den Iris-Datensatz und einen Linearen SVC-Klassifizierer verwenden, um zwei Arten von Irisen zu unterscheiden. Zunächst importieren wir die erforderlichen Bibliotheken und laden den Datensatz.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

Als nächstes fügen wir rauschende Merkmale zum Datensatz hinzu und teilen ihn in Trainings- und Testsets auf.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

Schließlich skalieren wir die Daten mit einem StandardScaler und trainieren einen Linearen SVC-Klassifizierer auf den Trainingsdaten.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
