# Entraîner et tester le classifieur K Plus Proches Voisins

Nous allons maintenant entraîner un classifieur K Plus Proches Voisins (KNN) à l'aide de la fonction `KNeighborsClassifier` de scikit-learn et le tester sur l'ensemble de test. Nous allons ensuite afficher le score de précision du classifieur.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
