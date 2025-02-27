# Kreuzvalidierte Schätzer

Einige Schätzer in scikit-learn haben eingebautes Kreuzvalidierungsvermögen. Diese kreuzvalidierten Schätzer wählen ihre Parameter automatisch durch Kreuzvalidierung, was den Modellauswahlprozess effizienter macht.

```python
from sklearn import linear_model, datasets

# Erstelle ein LassoCV-Objekt
lasso = linear_model.LassoCV()

# Lade den Diabetes-Datensatz
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Trainiere das LassoCV-Objekt auf dem Datensatz
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
