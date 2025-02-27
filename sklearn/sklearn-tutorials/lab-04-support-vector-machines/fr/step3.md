# Scores et probabilités

- Les SVM ne fournissent pas directement des estimations de probabilité, mais vous pouvez activer l'estimation de probabilité en définissant le paramètre `probability` sur `True` :

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- Vous pouvez ensuite utiliser la méthode `predict_proba` pour obtenir les probabilités de chaque classe :

```python
clf.predict_proba([[2., 2.]])
```

- Notez que l'estimation de probabilité est coûteuse et nécessite une validation croisée, utilisez donc cette fonction avec prudence.
