# Créer le pipeline

Ensuite, nous créons un pipeline composé d'une transformation de sélection de caractéristiques, d'un mise à l'échelle et d'une instance de SVM que nous combinons pour avoir un estimateur complet.

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
