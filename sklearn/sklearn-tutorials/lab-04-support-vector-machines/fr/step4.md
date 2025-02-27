# Problèmes déséquilibrés

- Les SVM peuvent gérer les problèmes déséquilibrés en ajustant le paramètre `class_weight` :

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
