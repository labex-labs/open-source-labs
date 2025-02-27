# Entrenar y probar el clasificador K-Nearest Neighbors

Ahora entrenaremos un clasificador K-Nearest Neighbors (KNN) utilizando la función `KNeighborsClassifier` de scikit-learn y lo probaremos en el conjunto de prueba. Luego imprimiremos la puntuación de precisión del clasificador.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
