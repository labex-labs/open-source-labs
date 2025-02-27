# Ein Pipeline mit Dimensionalitätsreduzierung und Klassifizierer erstellen

In diesem Schritt werden wir eine Pipeline mit einem Dimensionalitätsreduzierungsschritt und einem Klassifizierer erstellen und seine visuelle Darstellung anzeigen.

Zunächst importieren wir die erforderlichen Module:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Als nächstes definieren wir die Schritte der Pipeline:

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

Dann erstellen wir die Pipeline:

```python
pipe = Pipeline(steps)
```

Schließlich zeigen wir die visuelle Darstellung der Pipeline an:

```python
pipe
```
