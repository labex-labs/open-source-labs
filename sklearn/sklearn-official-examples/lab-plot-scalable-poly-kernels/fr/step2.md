# Établir un modèle de base

Nous allons entraîner un SVM linéaire sur les caractéristiques d'origine pour établir un modèle de base et afficher sa précision.

```python
from sklearn.svm import LinearSVC

# Entraîner un SVM linéaire sur les caractéristiques d'origine
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# Afficher la précision du modèle de base
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
