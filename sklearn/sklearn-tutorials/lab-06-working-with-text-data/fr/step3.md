# Extraction de caractéristiques

Pour représenter les données textuelles sous forme de vecteurs de caractéristiques, nous pouvons utiliser la représentation des sacs de mots. Cette représentation attribue un identifiant entier fixe à chaque mot de l'ensemble d'entraînement et compte le nombre d'occurrences de chaque mot dans chaque document. Nous pouvons extraire ces vecteurs de caractéristiques à l'aide de `CountVectorizer` de scikit-learn.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Extrait les vecteurs de caractéristiques
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

Maintenant, nous avons extrait les vecteurs de caractéristiques, et nous pouvons les utiliser pour entraîner notre modèle.
