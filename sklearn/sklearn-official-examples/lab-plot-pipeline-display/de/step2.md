# Ein Pipeline erstellen, die mehrere Vorverarbeitungsschritte und einen Klassifizierer verkettet

In diesem Schritt werden wir eine Pipeline erstellen, die mehrere Vorverarbeitungsschritte und einen Klassifizierer umfasst, und deren visuelle Darstellung anzeigen.

Zunächst importieren wir die erforderlichen Module:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Als nächstes definieren wir die Schritte der Pipeline:

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

Dann erstellen wir die Pipeline:

```python
pipe = Pipeline(steps)
```

Schließlich zeigen wir die visuelle Darstellung der Pipeline an:

```python
pipe
```
