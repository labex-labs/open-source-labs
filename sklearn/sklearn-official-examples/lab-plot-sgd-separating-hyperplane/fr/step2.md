# Entraînez le modèle SVM avec SGD

Ensuite, nous devons entraîner le modèle SVM en utilisant SGD. Nous allons utiliser la classe `SGDClassifier` de Scikit-learn pour entraîner le modèle. Nous allons définir le paramètre `loss` sur "hinge" pour utiliser l'algorithme SVM et le paramètre `alpha` sur 0,01 pour contrôler la force de régularisation. Nous allons également définir le paramètre `max_iter` sur 200 pour limiter le nombre d'itérations.

```python
# ajustez le modèle
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
