# Trainieren und Testen des K-Nearest Neighbors-Klassifizierers

Wir werden jetzt einen K-Nearest Neighbors (KNN)-Klassifizierer mit der Funktion `KNeighborsClassifier` von scikit-learn trainieren und ihn auf dem Testset testen. Anschließend werden wir die Genauigkeit des Klassifizierers ausgeben.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
