# Paramètre de notation

Scikit-learn fournit un paramètre `scoring` dans plusieurs outils d'évaluation de modèles, tels que la validation croisée et la recherche en grille. Le paramètre `scoring` contrôle la métrique appliquée aux estimateurs lors de l'évaluation.

Voici un exemple d'utilisation du paramètre `scoring` avec la validation croisée :

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
