# Modelltraining und -auswahl

Wir werden das RFECV-Objekt erstellen und die mit Kreuzvalidierung bewerteten Scores berechnen. Die Bewertungsstrategie "accuracy" optimiert den Anteil korrekt klassifizierter Proben. Wir werden die logistische Regression als Schätzer und die stratifizierte k-fache Kreuzvalidierung mit 5 Folds verwenden.

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # Mindestanzahl an Features, die berücksichtigt werden sollen
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Optimal number of features: {rfecv.n_features_}")
```
