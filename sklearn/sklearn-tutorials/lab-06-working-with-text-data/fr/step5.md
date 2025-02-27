# Évaluation du modèle

Pour évaluer les performances de notre modèle, nous pouvons utiliser un ensemble de test séparé. Nous pouvons charger l'ensemble de test en utilisant le même processus que pour l'ensemble d'entraînement.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

Maintenant, nous pouvons prétraiter l'ensemble de test et extraire les vecteurs de caractéristiques.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

Enfin, nous pouvons utiliser notre modèle entraîné pour effectuer des prédictions sur l'ensemble de test et calculer la précision.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
