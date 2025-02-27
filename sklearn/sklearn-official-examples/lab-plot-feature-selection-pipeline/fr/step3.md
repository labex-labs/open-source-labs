# Entraîner le pipeline

Nous allons maintenant entraîner le pipeline sur le sous-ensemble d'entraînement en utilisant la méthode `fit`. Pendant l'entraînement, la fonction `SelectKBest` sélectionnera les 3 caractéristiques les plus informatives sur la base de la valeur F de l'ANOVA, et la fonction `LinearSVC` entraînera un classifieur SVM linéaire sur les caractéristiques sélectionnées.

```python
anova_svm.fit(X_train, y_train)
```
