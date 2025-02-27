# Einfache Pipeline mit einem Vorverarbeitungsschritt und einem Klassifizierer erstellen

In diesem Schritt werden wir eine einfache Pipeline mit einem Vorverarbeitungsschritt und einem Klassifizierer erstellen und seine visuelle Darstellung anzeigen.

Zunächst importieren wir die erforderlichen Module:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Als nächstes definieren wir die Schritte der Pipeline:

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

Dann erstellen wir die Pipeline:

```python
pipe = Pipeline(steps)
```

Schließlich zeigen wir die visuelle Darstellung der Pipeline an:

```python
set_config(display="diagram")
pipe
```
