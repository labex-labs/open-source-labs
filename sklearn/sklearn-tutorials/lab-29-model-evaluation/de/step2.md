# Scoring-Parameter

Scikit-learn bietet in mehreren Modellbewertungs-Tools, wie Kreuzvalidierung und Gitter-Suche, einen `scoring`-Parameter. Der `scoring`-Parameter steuert die Metrik, die während der Bewertung auf die Estimatoren angewandt wird.

Hier ist ein Beispiel für die Verwendung des `scoring`-Parameters mit Kreuzvalidierung:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
