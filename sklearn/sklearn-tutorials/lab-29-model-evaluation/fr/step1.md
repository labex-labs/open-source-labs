# Méthode de notation d'Estimateur

La méthode de notation d'Estimateur est un critère d'évaluation par défaut fourni par scikit-learn pour chaque estimateur. Elle calcule une note qui représente la qualité des prédictions du modèle. Vous pouvez trouver plus d'informations à ce sujet dans la documentation de chaque estimateur.

Voici un exemple d'utilisation de la méthode `score` pour un estimateur :

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
