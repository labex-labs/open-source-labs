# Sélection de caractéristiques univariées

Ensuite, nous effectuerons une sélection de caractéristiques univariées avec le test F pour la notation des caractéristiques. Nous utiliserons la fonction de sélection par défaut pour sélectionner les quatre caractéristiques les plus significatives.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
