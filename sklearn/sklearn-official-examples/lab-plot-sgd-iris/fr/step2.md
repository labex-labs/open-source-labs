# Entraîner le modèle

Nous allons maintenant entraîner le modèle SGDClassifier sur l'ensemble de données iris à l'aide de la méthode fit(). Cette méthode prend les données d'entrée et les valeurs cibles en entrée et entraîne le modèle sur les données données.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
