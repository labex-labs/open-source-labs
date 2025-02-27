# Pipeline erstellen

Als nächstes erstellen wir eine Pipeline, die aus einem Feature-Selektions-Transformator, einem Skalierer und einer Instanz von SVM besteht, die wir zusammen kombinieren, um einen vollwertigen Schätzer zu erhalten.

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = Pipeline(
    [
        ("anova", SelectPercentile(f_classif)),
        ("scaler", StandardScaler()),
        ("svc", SVC(gamma="auto")),
    ]
)
```
