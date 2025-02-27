# Entraînement du modèle

Maintenant que nous avons nos vecteurs de caractéristiques, nous pouvons entraîner un modèle pour classifier les données textuelles. Dans cet exemple, nous utiliserons l'algorithme Multinomial Naive Bayes, qui est un algorithme populaire pour la classification de texte.

```python
from sklearn.naive_bayes import MultinomialNB

# Entraîne le modèle
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

Maintenant, notre modèle est entraîné et prêt pour la prédiction.
