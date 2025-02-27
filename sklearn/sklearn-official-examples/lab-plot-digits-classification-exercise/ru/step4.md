# Обучение и тестирование классификатора K-Nearest Neighbors

Теперь мы обучим классификатор K-Nearest Neighbors (KNN) с использованием функции `KNeighborsClassifier` из scikit-learn и протестируем его на тестовой выборке. Затем мы выведем показатель точности классификатора.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
