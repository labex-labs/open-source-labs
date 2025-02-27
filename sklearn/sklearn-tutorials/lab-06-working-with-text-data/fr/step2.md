# Prétraitement des données textuelles

Avant d'utiliser les données textuelles pour l'apprentissage automatique, nous devons les prétraiter. Cela implique plusieurs étapes, telles que la suppression de la ponctuation, la conversion de tout le texte en minuscules et la tokenisation du texte en mots individuels. Nous pouvons effectuer ces étapes de prétraitement à l'aide de `CountVectorizer` et `TfidfTransformer` de scikit-learn.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Prétraite les données textuelles
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

Maintenant, nos données textuelles sont prétraitées et prêtes pour l'extraction de caractéristiques.
