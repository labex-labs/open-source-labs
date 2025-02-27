# Univariate Feature Selection

Als nächstes werden wir die univariate Feature Selection mit F-Test zur Feature Bewertung durchführen. Wir werden die Standardauswahlfunktion verwenden, um die vier wichtigsten Features auszuwählen.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
