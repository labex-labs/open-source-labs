# Configurer le vectoriseur et réserver un ensemble de test

```python
# Créer le vectoriseur et limiter le nombre de fonctionnalités à un maximum raisonnable
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# Itérateur sur les fichiers SGML Reuters analysés.
data_stream = stream_reuters_documents()

# Nous apprenons une classification binaire entre la classe "acq" et toutes les autres.
# "acq" a été choisi car il est plus ou moins régulièrement réparti dans les fichiers Reuters.
# Pour d'autres ensembles de données, il faudrait prendre soin de créer un ensemble de test avec
# une partie réaliste d'instances positives.
all_classes = np.array([0, 1])
positive_class = "acq"

# Voici quelques classifieurs qui prennent en charge la méthode `partial_fit`
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# statistiques sur les données de test
test_stats = {"n_test": 0, "n_test_pos": 0}

# Tout d'abord, nous réservons un certain nombre d'exemples pour estimer la précision
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("L'ensemble de test est composé de %d documents (%d positifs)" % (len(y_test), sum(y_test)))
```
