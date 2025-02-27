# Fonctions de métrique

Le module `metrics` de scikit-learn implémente plusieurs fonctions pour évaluer l'erreur de prédiction dans des buts spécifiques. Ces fonctions peuvent être utilisées pour calculer la qualité des prédictions faites par un modèle.

Voici un exemple d'utilisation de la fonction `accuracy_score` du module `metrics` :

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
