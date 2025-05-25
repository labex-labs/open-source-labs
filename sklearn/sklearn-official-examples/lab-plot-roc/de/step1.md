# Laden und Vorbereiten der Daten

Lassen Sie uns beginnen, indem wir den Iris-Datensatz laden und ihn für die 计算 der Qualität eines Klassifizierers mit der ROC-Metrik vorbereiten.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
y = iris.target_names[y]

# Fügen Sie rauschende Merkmale hinzu, um das Problem schwieriger zu machen
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
n_classes = len(np.unique(y))
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

# Teilen Sie die Daten in Trainings- und Testsets auf
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y, random_state=0)
```
